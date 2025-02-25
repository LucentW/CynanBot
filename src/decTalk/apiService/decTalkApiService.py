import asyncio
import os
import re
import uuid
from asyncio import AbstractEventLoop, CancelledError as AsyncioCancelledError
from asyncio import TimeoutError as AsyncioTimeoutError
from asyncio.subprocess import Process
from typing import ByteString, Pattern

import aiofiles
import aiofiles.os
import aiofiles.ospath
import psutil

from .decTalkApiServiceInterface import DecTalkApiServiceInterface
from ..exceptions import DecTalkExecutableIsMissingException, DecTalkFailedToGenerateSpeechFileException
from ..settings.decTalkSettingsRepositoryInterface import DecTalkSettingsRepositoryInterface
from ...misc import utils as utils
from ...timber.timberInterface import TimberInterface
from ...tts.directoryProvider.ttsDirectoryProviderInterface import TtsDirectoryProviderInterface
from ...tts.ttsProvider import TtsProvider


class DecTalkApiService(DecTalkApiServiceInterface):

    def __init__(
        self,
        eventLoop: AbstractEventLoop,
        decTalkSettingsRepository: DecTalkSettingsRepositoryInterface,
        timber: TimberInterface,
        ttsDirectoryProvider: TtsDirectoryProviderInterface,
        fileExtension: str = 'wav'
    ):
        if not isinstance(eventLoop, AbstractEventLoop):
            raise TypeError(f'eventLoop argument is malformed: \"{eventLoop}\"')
        elif not isinstance(decTalkSettingsRepository, DecTalkSettingsRepositoryInterface):
            raise TypeError(f'decTalkSettingsRepository argument is malformed: \"{decTalkSettingsRepository}\"')
        elif not isinstance(timber, TimberInterface):
            raise TypeError(f'timber argument is malformed: \"{timber}\"')
        elif not isinstance(ttsDirectoryProvider, TtsDirectoryProviderInterface):
            raise TypeError(f'ttsDirectoryProvider argument is malformed: \"{ttsDirectoryProvider}\"')
        elif not utils.isValidStr(fileExtension):
            raise TypeError(f'fileExtension argument is malformed: \"{fileExtension}\"')

        self.__eventLoop: AbstractEventLoop = eventLoop
        self.__decTalkSettingsRepository: DecTalkSettingsRepositoryInterface = decTalkSettingsRepository
        self.__timber: TimberInterface = timber
        self.__ttsDirectoryProvider: TtsDirectoryProviderInterface = ttsDirectoryProvider
        self.__fileExtension: str = fileExtension

        self.__fileNameRegEx: Pattern = re.compile(r'[^a-z0-9]', re.IGNORECASE)

    async def __createDirectories(self, filePath: str):
        if await aiofiles.ospath.exists(
            path = filePath,
            loop = self.__eventLoop
        ):
            return

        await aiofiles.os.makedirs(
            name = filePath,
            loop = self.__eventLoop
        )

        self.__timber.log('DecTalkApiService', f'Created new directories ({filePath=})')

    async def __generateFileName(self) -> str:
        fileName = self.__fileNameRegEx.sub('', str(uuid.uuid4())).casefold()
        return f'{fileName}.{self.__fileExtension}'

    async def generateSpeechFile(self, text: str) -> str:
        if not utils.isValidStr(text):
            raise TypeError(f'text argument is malformed: \"{text}\"')

        self.__timber.log('DecTalkApiService', f'Generating speech... ({text=})')

        pathToDecTalk = await self.__decTalkSettingsRepository.requireDecTalkExecutablePath()

        if not await aiofiles.ospath.exists(
            path = pathToDecTalk,
            loop = self.__eventLoop
        ):
            raise DecTalkExecutableIsMissingException(f'Couldn\'t find DecTalk executable ({pathToDecTalk=})')

        filePath = await self.__ttsDirectoryProvider.getFullTtsDirectoryFor(TtsProvider.DEC_TALK)
        await self.__createDirectories(filePath)

        fileName = await self.__generateFileName()
        fullFilePath = os.path.normpath(f'{filePath}/{fileName}')

        decTalkProcess: Process | None = None
        outputTuple: tuple[ByteString, ByteString] | None = None
        exception: BaseException | None = None

        command = f'{os.path.normpath(pathToDecTalk)} -w \"{fullFilePath}\" -pre \"[:phone on]\" \"{text}\"'

        try:
            decTalkProcess = await asyncio.create_subprocess_shell(
                cmd = command,
                stdout = asyncio.subprocess.PIPE,
                stderr = asyncio.subprocess.PIPE
            )

            outputTuple = await asyncio.wait_for(
                fut = decTalkProcess.communicate(),
                timeout = 3
            )
        except BaseException as e:
            exception = e

        if isinstance(exception, AsyncioTimeoutError) or isinstance(exception, AsyncioCancelledError) or isinstance(exception, TimeoutError):
            await self.__killDecTalkProcess(decTalkProcess)

        outputString: str | None = None

        if outputTuple is not None and len(outputTuple) >= 2:
            outputString = outputTuple[1].decode('utf-8').strip()

        self.__timber.log('DecTalkApiService', f'Ran DecTalk system command ({command=}) ({outputString=}) ({exception=})')

        if not await aiofiles.ospath.exists(
            path = fullFilePath,
            loop = self.__eventLoop
        ):
            raise DecTalkFailedToGenerateSpeechFileException(f'Failed to generate speech file ({fileName=}) ({filePath=}) ({command=}) ({outputString=}) ({exception=})')

        return fullFilePath

    async def __killDecTalkProcess(self, decTalkProcess: Process | None):
        if decTalkProcess is None:
            self.__timber.log('DecTalkApiService', f'Went to kill the DecTalk process, but the process is None ({decTalkProcess=})')
            return
        elif not isinstance(decTalkProcess, Process):
            raise TypeError(f'process argument is malformed: \"{decTalkProcess}\"')
        elif decTalkProcess.returncode is not None:
            self.__timber.log('DecTalkApiService', f'Went to kill a DecTalk process, but the process has a return code ({decTalkProcess=}) ({decTalkProcess.returncode=})')
            return

        self.__timber.log('DecTalkApiService', f'Killing DecTalk process ({decTalkProcess=})...')
        parent = psutil.Process(decTalkProcess.pid)
        childCount = 0

        for child in parent.children(recursive = True):
            child.terminate()
            childCount += 1

        parent.terminate()
        self.__timber.log('DecTalkApiService', f'Finished killing DecTalk process ({decTalkProcess=}) ({childCount=})')
