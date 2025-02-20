from .chatterPreferredTtsHelperInterface import ChatterPreferredTtsHelperInterface
from ..models.chatterPrefferedTts import ChatterPreferredTts
from ..repository.chatterPreferredTtsRepositoryInterface import ChatterPreferredTtsRepositoryInterface
from ..settings.chatterPreferredTtsSettingsRepositoryInterface import ChatterPreferredTtsSettingsRepositoryInterface
from ...misc import utils as utils


class ChatterPreferredTtsHelper(ChatterPreferredTtsHelperInterface):

    def __init__(
        self,
        chatterPreferredTtsRepository: ChatterPreferredTtsRepositoryInterface,
        chatterPreferredTtsSettings: ChatterPreferredTtsSettingsRepositoryInterface
    ):
        if not isinstance(chatterPreferredTtsRepository, ChatterPreferredTtsRepositoryInterface):
            raise TypeError(f'chatterPreferredTtsRepository argument is malformed: \"{chatterPreferredTtsRepository}\"')
        elif not isinstance(chatterPreferredTtsSettings, ChatterPreferredTtsSettingsRepositoryInterface):
            raise TypeError(f'chatterPreferredTtsSettings argument is malformed: \"{chatterPreferredTtsSettings}\"')

        self.__chatterPreferredTtsRepository: ChatterPreferredTtsRepositoryInterface = chatterPreferredTtsRepository
        self.__chatterPreferredTtsSettings: ChatterPreferredTtsSettingsRepositoryInterface = chatterPreferredTtsSettings

    async def get(
        self,
        chatterUserId: str,
        twitchChannelId: str
    ) -> ChatterPreferredTts | None:
        if not utils.isValidStr(chatterUserId):
            raise TypeError(f'chatterUserId argument is malformed: \"{chatterUserId}\"')
        elif not utils.isValidStr(twitchChannelId):
            raise TypeError(f'twitchChannelId argument is malformed: \"{twitchChannelId}\"')

        if not await self.__chatterPreferredTtsSettings.isEnabled():
            return None

        return await self.__chatterPreferredTtsRepository.get(
            chatterUserId = chatterUserId,
            twitchChannelId = twitchChannelId
        )
