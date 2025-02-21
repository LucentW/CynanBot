from frozenlist import FrozenList

from .absChatCommand import AbsChatCommand
from ..aniv.anivSettingsRepositoryInterface import AnivSettingsRepositoryInterface
from ..aniv.mostRecentAnivMessageRepositoryInterface import MostRecentAnivMessageRepositoryInterface
from ..chatterPreferredTts.repository.chatterPreferredTtsRepositoryInterface import \
    ChatterPreferredTtsRepositoryInterface
from ..chatterPreferredTts.settings.chatterPreferredTtsSettingsRepositoryInterface import \
    ChatterPreferredTtsSettingsRepositoryInterface
from ..cheerActions.cheerActionSettingsRepositoryInterface import CheerActionSettingsRepositoryInterface
from ..cheerActions.cheerActionsRepositoryInterface import CheerActionsRepositoryInterface
from ..contentScanner.bannedWordsRepositoryInterface import BannedWordsRepositoryInterface
from ..crowdControl.bizhawk.bizhawkSettingsRepositoryInterface import BizhawkSettingsRepositoryInterface
from ..crowdControl.crowdControlSettingsRepositoryInterface import CrowdControlSettingsRepositoryInterface
from ..decTalk.settings.decTalkSettingsRepositoryInterface import DecTalkSettingsRepositoryInterface
from ..funtoon.tokens.funtoonTokensRepositoryInterface import FuntoonTokensRepositoryInterface
from ..google.settings.googleSettingsRepositoryInterface import GoogleSettingsRepositoryInterface
from ..halfLife.service.halfLifeServiceInterface import HalfLifeServiceInterface
from ..halfLife.settings.halfLifeSettingsRepositoryInterface import HalfLifeSettingsRepositoryInterface
from ..language.wordOfTheDay.wordOfTheDayRepositoryInterface import WordOfTheDayRepositoryInterface
from ..location.locationsRepositoryInterface import LocationsRepositoryInterface
from ..microsoftSam.settings.microsoftSamSettingsRepositoryInterface import MicrosoftSamSettingsRepositoryInterface
from ..misc.administratorProviderInterface import AdministratorProviderInterface
from ..misc.authRepository import AuthRepository
from ..misc.clearable import Clearable
from ..misc.generalSettingsRepository import GeneralSettingsRepository
from ..mostRecentChat.mostRecentChatsRepositoryInterface import MostRecentChatsRepositoryInterface
from ..soundPlayerManager.randomizerHelper.soundPlayerRandomizerHelperInterface import \
    SoundPlayerRandomizerHelperInterface
from ..soundPlayerManager.settings.soundPlayerSettingsRepositoryInterface import SoundPlayerSettingsRepositoryInterface
from ..storage.psql.psqlCredentialsProviderInterface import PsqlCredentialsProviderInterface
from ..streamAlertsManager.streamAlertsSettingsRepositoryInterface import StreamAlertsSettingsRepositoryInterface
from ..streamElements.settings.streamElementsSettingsRepositoryInterface import \
    StreamElementsSettingsRepositoryInterface
from ..streamElements.userKeyRepository.streamElementsUserKeyRepositoryInterface import \
    StreamElementsUserKeyRepositoryInterface
from ..supStreamer.supStreamerRepositoryInterface import SupStreamerRepositoryInterface
from ..timber.timberInterface import TimberInterface
from ..timeout.timeoutActionHistoryRepositoryInterface import \
    TimeoutActionHistoryRepositoryInterface
from ..timeout.timeoutActionSettingsRepositoryInterface import \
    TimeoutActionSettingsRepositoryInterface
from ..trivia.triviaRepositories.openTriviaDatabase.openTriviaDatabaseSessionTokenRepositoryInterface import \
    OpenTriviaDatabaseSessionTokenRepositoryInterface
from ..trivia.triviaSettingsRepositoryInterface import TriviaSettingsRepositoryInterface
from ..trollmoji.trollmojiHelperInterface import TrollmojiHelperInterface
from ..trollmoji.trollmojiSettingsRepositoryInterface import TrollmojiSettingsRepositoryInterface
from ..tts.ttsSettingsRepositoryInterface import TtsSettingsRepositoryInterface
from ..ttsMonster.keyAndUserIdRepository.ttsMonsterKeyAndUserIdRepositoryInterface import \
    TtsMonsterKeyAndUserIdRepositoryInterface
from ..ttsMonster.settings.ttsMonsterSettingsRepositoryInterface import TtsMonsterSettingsRepositoryInterface
from ..twitch.channelEditors.twitchChannelEditorsRepositoryInterface import \
    TwitchChannelEditorsRepositoryInterface
from ..twitch.configuration.twitchContext import TwitchContext
from ..twitch.emotes.twitchEmotesHelperInterface import TwitchEmotesHelperInterface
from ..twitch.followingStatus.twitchFollowingStatusRepositoryInterface import TwitchFollowingStatusRepositoryInterface
from ..twitch.isLive.isLiveOnTwitchRepositoryInterface import IsLiveOnTwitchRepositoryInterface
from ..twitch.subscribers.twitchSubscriptionsRepositoryInterface import TwitchSubscriptionsRepositoryInterface
from ..twitch.tokens.twitchTokensRepositoryInterface import TwitchTokensRepositoryInterface
from ..twitch.twitchUtilsInterface import TwitchUtilsInterface
from ..users.addOrRemoveUserDataHelper import AddOrRemoveUserDataHelperInterface
from ..users.userIdsRepositoryInterface import UserIdsRepositoryInterface
from ..users.usersRepositoryInterface import UsersRepositoryInterface
from ..weather.weatherRepositoryInterface import WeatherRepositoryInterface


class ClearCachesChatCommand(AbsChatCommand):

    def __init__(
        self,
        addOrRemoveUserDataHelper: AddOrRemoveUserDataHelperInterface,
        administratorProvider: AdministratorProviderInterface,
        anivSettingsRepository: AnivSettingsRepositoryInterface | None,
        authRepository: AuthRepository,
        bannedWordsRepository: BannedWordsRepositoryInterface | None,
        bizhawkSettingsRepository: BizhawkSettingsRepositoryInterface | None,
        chatterPreferredTtsRepository: ChatterPreferredTtsRepositoryInterface | None,
        chatterPreferredTtsSettingsRepository: ChatterPreferredTtsSettingsRepositoryInterface | None,
        cheerActionSettingsRepository: CheerActionSettingsRepositoryInterface | None,
        cheerActionsRepository: CheerActionsRepositoryInterface | None,
        crowdControlSettingsRepository: CrowdControlSettingsRepositoryInterface | None,
        decTalkSettingsRepository: DecTalkSettingsRepositoryInterface | None,
        funtoonTokensRepository: FuntoonTokensRepositoryInterface | None,
        generalSettingsRepository: GeneralSettingsRepository,
        googleSettingsRepository: GoogleSettingsRepositoryInterface | None,
        halfLifeService: HalfLifeServiceInterface | None,
        halfLifeSettingsRepository: HalfLifeSettingsRepositoryInterface | None,
        isLiveOnTwitchRepository: IsLiveOnTwitchRepositoryInterface | None,
        locationsRepository: LocationsRepositoryInterface | None,
        microsoftSamSettingsRepository: MicrosoftSamSettingsRepositoryInterface | None,
        mostRecentAnivMessageRepository: MostRecentAnivMessageRepositoryInterface | None,
        mostRecentChatsRepository: MostRecentChatsRepositoryInterface | None,
        openTriviaDatabaseSessionTokenRepository: OpenTriviaDatabaseSessionTokenRepositoryInterface | None,
        psqlCredentialsProvider: PsqlCredentialsProviderInterface | None,
        soundPlayerRandomizerHelper: SoundPlayerRandomizerHelperInterface | None,
        soundPlayerSettingsRepository: SoundPlayerSettingsRepositoryInterface | None,
        streamAlertsSettingsRepository: StreamAlertsSettingsRepositoryInterface | None,
        streamElementsSettingsRepository: StreamElementsSettingsRepositoryInterface | None,
        streamElementsUserKeyRepository: StreamElementsUserKeyRepositoryInterface | None,
        supStreamerRepository: SupStreamerRepositoryInterface | None,
        timber: TimberInterface,
        timeoutActionHistoryRepository: TimeoutActionHistoryRepositoryInterface | None,
        timeoutActionSettingsRepository: TimeoutActionSettingsRepositoryInterface | None,
        triviaSettingsRepository: TriviaSettingsRepositoryInterface | None,
        trollmojiHelper: TrollmojiHelperInterface | None,
        trollmojiSettingsRepository: TrollmojiSettingsRepositoryInterface | None,
        ttsMonsterKeyAndUserIdRepository: TtsMonsterKeyAndUserIdRepositoryInterface | None,
        ttsMonsterSettingsRepository: TtsMonsterSettingsRepositoryInterface | None,
        ttsSettingsRepository: TtsSettingsRepositoryInterface | None,
        twitchChannelEditorsRepository: TwitchChannelEditorsRepositoryInterface | None,
        twitchEmotesHelper: TwitchEmotesHelperInterface | None,
        twitchFollowingStatusRepository: TwitchFollowingStatusRepositoryInterface | None,
        twitchSubscriptionsRepository: TwitchSubscriptionsRepositoryInterface | None,
        twitchTokensRepository: TwitchTokensRepositoryInterface | None,
        twitchUtils: TwitchUtilsInterface,
        userIdsRepository: UserIdsRepositoryInterface,
        usersRepository: UsersRepositoryInterface,
        weatherRepository: WeatherRepositoryInterface | None,
        wordOfTheDayRepository: WordOfTheDayRepositoryInterface | None
    ):
        if not isinstance(addOrRemoveUserDataHelper, AddOrRemoveUserDataHelperInterface):
            raise TypeError(f'addOrRemoveUserDataHelper argument is malformed: \"{addOrRemoveUserDataHelper}\"')
        elif not isinstance(administratorProvider, AdministratorProviderInterface):
            raise TypeError(f'administratorProvider argument is malformed: \"{administratorProvider}\"')
        elif anivSettingsRepository is not None and not isinstance(anivSettingsRepository, AnivSettingsRepositoryInterface):
            raise TypeError(f'anivSettingsRepository argument is malformed: \"{anivSettingsRepository}\"')
        elif not isinstance(authRepository, AuthRepository):
            raise TypeError(f'authRepository argument is malformed: \"{authRepository}\"')
        elif bannedWordsRepository is not None and not isinstance(bannedWordsRepository, BannedWordsRepositoryInterface):
            raise TypeError(f'bannedWordsRepository argument is malformed: \"{bannedWordsRepository}\"')
        elif bizhawkSettingsRepository is not None and not isinstance(bizhawkSettingsRepository, BizhawkSettingsRepositoryInterface):
            raise TypeError(f'bizhawkSettingsRepository argument is malformed: \"{bizhawkSettingsRepository}\"')
        elif chatterPreferredTtsRepository is not None and not isinstance(chatterPreferredTtsRepository, ChatterPreferredTtsSettingsRepositoryInterface):
            raise TypeError(f'chatterPreferredTtsRepository argument is malformed: \"{chatterPreferredTtsRepository}\"')
        elif chatterPreferredTtsSettingsRepository is not None and not isinstance(chatterPreferredTtsSettingsRepository, ChatterPreferredTtsSettingsRepositoryInterface):
            raise TypeError(f'chatterPreferredTtsSettingsRepository argument is malformed: \"{chatterPreferredTtsSettingsRepository}\"')
        elif cheerActionSettingsRepository is not None and not isinstance(cheerActionSettingsRepository, CheerActionSettingsRepositoryInterface):
            raise TypeError(f'cheerActionSettingsRepository argument is malformed: \"{cheerActionSettingsRepository}\"')
        elif cheerActionsRepository is not None and not isinstance(cheerActionsRepository, CheerActionsRepositoryInterface):
            raise TypeError(f'cheerActionsRepository argument is malformed: \"{cheerActionsRepository}\"')
        elif crowdControlSettingsRepository is not None and not isinstance(crowdControlSettingsRepository, CrowdControlSettingsRepositoryInterface):
            raise TypeError(f'crowdControlSettingsRepository argument is malformed: \"{crowdControlSettingsRepository}\"')
        elif decTalkSettingsRepository is not None and not isinstance(decTalkSettingsRepository, DecTalkSettingsRepositoryInterface):
            raise TypeError(f'decTalkSettingsRepository argument is malformed: \"{decTalkSettingsRepository}\"')
        elif funtoonTokensRepository is not None and not isinstance(funtoonTokensRepository, FuntoonTokensRepositoryInterface):
            raise TypeError(f'funtoonTokensRepository argument is malformed: \"{funtoonTokensRepository}\"')
        elif not isinstance(generalSettingsRepository, GeneralSettingsRepository):
            raise TypeError(f'generalSettingsRepository argument is malformed: \"{generalSettingsRepository}\"')
        elif googleSettingsRepository is not None and not isinstance(googleSettingsRepository, GoogleSettingsRepositoryInterface):
            raise TypeError(f'googleSettingsRepository argument is malformed: \"{googleSettingsRepository}\"')
        elif halfLifeService is not None and not isinstance(halfLifeService, HalfLifeServiceInterface):
            raise TypeError(f'halfLifeService argument is malformed: \"{halfLifeService}\"')
        elif halfLifeSettingsRepository is not None and not isinstance(halfLifeSettingsRepository, HalfLifeSettingsRepositoryInterface):
            raise TypeError(f'halfLifeSettingsRepository argument is malformed: \"{halfLifeSettingsRepository}\"')
        elif isLiveOnTwitchRepository is not None and not isinstance(isLiveOnTwitchRepository, IsLiveOnTwitchRepositoryInterface):
            raise TypeError(f'isLiveOnTwitchRepository argument is malformed: \"{isLiveOnTwitchRepository}\"')
        elif locationsRepository is not None and not isinstance(locationsRepository, LocationsRepositoryInterface):
            raise TypeError(f'locationsRepository argument is malformed: \"{locationsRepository}\"')
        elif microsoftSamSettingsRepository is not None and not isinstance(microsoftSamSettingsRepository, MicrosoftSamSettingsRepositoryInterface):
            raise TypeError(f'microsoftSamSettingsRepository argument is malformed: \"{microsoftSamSettingsRepository}\"')
        elif mostRecentAnivMessageRepository is not None and not isinstance(mostRecentAnivMessageRepository, MostRecentAnivMessageRepositoryInterface):
            raise TypeError(f'mostRecentAnivMessageRepository argument is malformed: \"{mostRecentAnivMessageRepository}\"')
        elif mostRecentChatsRepository is not None and not isinstance(mostRecentChatsRepository, MostRecentChatsRepositoryInterface):
            raise TypeError(f'mostRecentChatsRepository argument is malformed: \"{mostRecentChatsRepository}\"')
        elif openTriviaDatabaseSessionTokenRepository is not None and not isinstance(openTriviaDatabaseSessionTokenRepository, OpenTriviaDatabaseSessionTokenRepositoryInterface):
            raise TypeError(f'openTriviaDatabaseSessionTokenRepository argument is malformed: \"{openTriviaDatabaseSessionTokenRepository}\"')
        elif psqlCredentialsProvider is not None and not isinstance(psqlCredentialsProvider, PsqlCredentialsProviderInterface):
            raise TypeError(f'psqlCredentialsProvider argument is malformed: \"{psqlCredentialsProvider}\"')
        elif soundPlayerRandomizerHelper is not None and not isinstance(soundPlayerRandomizerHelper, SoundPlayerRandomizerHelperInterface):
            raise TypeError(f'soundPlayerRandomizerHelper argument is malformed: \"{soundPlayerRandomizerHelper}\"')
        elif soundPlayerSettingsRepository is not None and not isinstance(soundPlayerSettingsRepository, SoundPlayerSettingsRepositoryInterface):
            raise TypeError(f'soundPlayerSettingsRepository argument is malformed: \"{soundPlayerSettingsRepository}\"')
        elif streamAlertsSettingsRepository is not None and not isinstance(streamAlertsSettingsRepository, StreamAlertsSettingsRepositoryInterface):
            raise TypeError(f'streamAlertsSettingsRepository argument is malformed: \"{streamAlertsSettingsRepository}\"')
        elif streamElementsSettingsRepository is not None and not isinstance(streamElementsSettingsRepository, StreamElementsSettingsRepositoryInterface):
            raise TypeError(f'streamElementsSettingsRepository argument is malformed: \"{streamElementsSettingsRepository}\"')
        elif streamElementsUserKeyRepository is not None and not isinstance(streamElementsUserKeyRepository, StreamElementsUserKeyRepositoryInterface):
            raise TypeError(f'streamElementsUserKeyRepository argument is malformed: \"{streamElementsUserKeyRepository}\"')
        elif supStreamerRepository is not None and not isinstance(supStreamerRepository, SupStreamerRepositoryInterface):
            raise TypeError(f'supStreamerRepository argument is malformed: \"{supStreamerRepository}\"')
        elif not isinstance(timber, TimberInterface):
            raise TypeError(f'timber argument is malformed: \"{timber}\"')
        elif timeoutActionHistoryRepository is not None and not isinstance(timeoutActionHistoryRepository, TimeoutActionHistoryRepositoryInterface):
            raise TypeError(f'timeoutActionHistoryRepository argument is malformed: \"{timeoutActionHistoryRepository}\"')
        elif timeoutActionSettingsRepository is not None and not isinstance(timeoutActionSettingsRepository, TimeoutActionSettingsRepositoryInterface):
            raise TypeError(f'timeoutActionSettingsRepository argument is malformed: \"{timeoutActionSettingsRepository}\"')
        elif triviaSettingsRepository is not None and not isinstance(triviaSettingsRepository, TriviaSettingsRepositoryInterface):
            raise TypeError(f'triviaSettingsRepository argument is malformed: \"{triviaSettingsRepository}\"')
        elif trollmojiHelper is not None and not isinstance(trollmojiHelper, TrollmojiHelperInterface):
            raise TypeError(f'trollmojiHelper argument is malformed: \"{trollmojiHelper}\"')
        elif trollmojiSettingsRepository is not None and not isinstance(trollmojiSettingsRepository, TrollmojiSettingsRepositoryInterface):
            raise TypeError(f'trollmojiSettingsRepository argument is malformed: \"{trollmojiSettingsRepository}\"')
        elif ttsMonsterKeyAndUserIdRepository is not None and not isinstance(ttsMonsterKeyAndUserIdRepository, TtsMonsterKeyAndUserIdRepositoryInterface):
            raise TypeError(f'ttsMonsterKeyAndUserIdRepository argument is malformed: \"{ttsMonsterKeyAndUserIdRepository}\"')
        elif ttsMonsterSettingsRepository is not None and not isinstance(ttsMonsterSettingsRepository, TtsMonsterSettingsRepositoryInterface):
            raise TypeError(f'ttsMonsterSettingsRepository argument is malformed: \"{ttsMonsterSettingsRepository}\"')
        elif ttsSettingsRepository is not None and not isinstance(ttsSettingsRepository, TtsSettingsRepositoryInterface):
            raise TypeError(f'ttsSettingsRepository argument is malformed: \"{ttsSettingsRepository}\"')
        elif twitchChannelEditorsRepository is not None and not isinstance(twitchChannelEditorsRepository, TwitchChannelEditorsRepositoryInterface):
            raise TypeError(f'twitchChannelEditorsRepository argument is malformed: \"{twitchChannelEditorsRepository}\"')
        elif twitchEmotesHelper is not None and not isinstance(twitchEmotesHelper, TwitchEmotesHelperInterface):
            raise TypeError(f'twitchEmotesHelper argument is malformed: \"{twitchEmotesHelper}\"')
        elif twitchFollowingStatusRepository is not None and not isinstance(twitchFollowingStatusRepository, TwitchFollowingStatusRepositoryInterface):
            raise TypeError(f'twitchFollowingStatusRepository argument is malformed: \"{twitchFollowingStatusRepository}\"')
        elif twitchSubscriptionsRepository is not None and not isinstance(twitchSubscriptionsRepository, TwitchSubscriptionsRepositoryInterface):
            raise TypeError(f'twitchSubscriptionsRepository argument is malformed: \"{twitchSubscriptionsRepository}\"')
        elif twitchTokensRepository is not None and not isinstance(twitchTokensRepository, TwitchTokensRepositoryInterface):
            raise TypeError(f'twitchTokensRepository argument is malformed: \"{twitchTokensRepository}\"')
        elif not isinstance(twitchUtils, TwitchUtilsInterface):
            raise TypeError(f'twitchUtils argument is malformed: \"{twitchUtils}\"')
        elif not isinstance(userIdsRepository, UserIdsRepositoryInterface):
            raise TypeError(f'userIdsRepository argument is malformed: \"{userIdsRepository}\"')
        elif not isinstance(usersRepository, UsersRepositoryInterface):
            raise TypeError(f'usersRepository argument is malformed: \"{usersRepository}\"')
        elif weatherRepository is not None and not isinstance(weatherRepository, WeatherRepositoryInterface):
            raise TypeError(f'weatherRepository argument is malformed: \"{weatherRepository}\"')
        elif wordOfTheDayRepository is not None and not isinstance(wordOfTheDayRepository, WordOfTheDayRepositoryInterface):
            raise TypeError(f'wordOfTheDayRepository argument is malformed: \"{wordOfTheDayRepository}\"')

        self.__administratorProvider: AdministratorProviderInterface = administratorProvider
        self.__timber: TimberInterface = timber
        self.__twitchUtils: TwitchUtilsInterface = twitchUtils
        self.__usersRepository: UsersRepositoryInterface = usersRepository

        self.__clearables: FrozenList[Clearable | None] = FrozenList()
        self.__clearables.append(addOrRemoveUserDataHelper)
        self.__clearables.append(administratorProvider)
        self.__clearables.append(anivSettingsRepository)
        self.__clearables.append(authRepository)
        self.__clearables.append(bannedWordsRepository)
        self.__clearables.append(bizhawkSettingsRepository)
        self.__clearables.append(chatterPreferredTtsRepository)
        self.__clearables.append(chatterPreferredTtsSettingsRepository)
        self.__clearables.append(cheerActionSettingsRepository)
        self.__clearables.append(cheerActionsRepository)
        self.__clearables.append(crowdControlSettingsRepository)
        self.__clearables.append(decTalkSettingsRepository)
        self.__clearables.append(funtoonTokensRepository)
        self.__clearables.append(generalSettingsRepository)
        self.__clearables.append(googleSettingsRepository)
        self.__clearables.append(halfLifeService)
        self.__clearables.append(halfLifeSettingsRepository)
        self.__clearables.append(isLiveOnTwitchRepository)
        self.__clearables.append(locationsRepository)
        self.__clearables.append(microsoftSamSettingsRepository)
        self.__clearables.append(mostRecentAnivMessageRepository)
        self.__clearables.append(mostRecentChatsRepository)
        self.__clearables.append(openTriviaDatabaseSessionTokenRepository)
        self.__clearables.append(psqlCredentialsProvider)
        self.__clearables.append(soundPlayerRandomizerHelper)
        self.__clearables.append(soundPlayerSettingsRepository)
        self.__clearables.append(streamAlertsSettingsRepository)
        self.__clearables.append(streamElementsSettingsRepository)
        self.__clearables.append(streamElementsUserKeyRepository)
        self.__clearables.append(supStreamerRepository)
        self.__clearables.append(timeoutActionHistoryRepository)
        self.__clearables.append(timeoutActionSettingsRepository)
        self.__clearables.append(triviaSettingsRepository)
        self.__clearables.append(trollmojiHelper)
        self.__clearables.append(trollmojiSettingsRepository)
        self.__clearables.append(ttsMonsterKeyAndUserIdRepository)
        self.__clearables.append(ttsMonsterSettingsRepository)
        self.__clearables.append(ttsSettingsRepository)
        self.__clearables.append(twitchChannelEditorsRepository)
        self.__clearables.append(twitchEmotesHelper)
        self.__clearables.append(twitchFollowingStatusRepository)
        self.__clearables.append(twitchSubscriptionsRepository)
        self.__clearables.append(twitchTokensRepository)
        self.__clearables.append(userIdsRepository)
        self.__clearables.append(usersRepository)
        self.__clearables.append(weatherRepository)
        self.__clearables.append(wordOfTheDayRepository)
        self.__clearables.freeze()

        badIndices: list[int] = list()
        for index, clearable in enumerate(self.__clearables):
            if clearable is not None and not isinstance(clearable, Clearable):
                badIndices.append(index)

        if len(badIndices) >= 1:
            raise TypeError(f'Encountered {len(badIndices)} instance(s) in clearables list that aren\'t Clearable: {badIndices}')

    async def handleChatCommand(self, ctx: TwitchContext):
        user = await self.__usersRepository.getUserAsync(ctx.getTwitchChannelName())
        administrator = await self.__administratorProvider.getAdministratorUserId()

        if administrator != ctx.getAuthorId():
            self.__timber.log('ClearCachesCommand', f'Attempted use of !clearcaches command by {ctx.getAuthorName()}:{ctx.getAuthorId()} in {user.handle}')
            return

        for clearable in self.__clearables:
            if clearable is not None:
                await clearable.clearCaches()

        await self.__twitchUtils.safeSend(
            messageable = ctx,
            message = 'ⓘ All caches cleared',
            replyMessageId = await ctx.getMessageId()
        )

        self.__timber.log('ClearCachesCommand', f'Handled !clearcaches command for {ctx.getAuthorName()}:{ctx.getAuthorId()} in {user.handle}')
