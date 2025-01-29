from .accessLevelCheckingRepositoryInterface import AccessLevelCheckingRepositoryInterface
from ..misc import utils
from ..twitch.configuration.twitchMessage import TwitchMessage
from ..twitch.followingStatus.twitchFollowingStatusRepositoryInterface import TwitchFollowingStatusRepositoryInterface
from ..twitch.ircTagsParser.twitchIrcTags import TwitchIrcTags
from ..twitch.tokens.twitchTokensRepositoryInterface import TwitchTokensRepositoryInterface
from ..users.accessLevel.accessLevel import AccessLevel


class AccessLevelCheckingRepository(AccessLevelCheckingRepositoryInterface):

    def __init__(
        self,
        twitchFollowingStatusRepository: TwitchFollowingStatusRepositoryInterface,
        twitchTokensRepository: TwitchTokensRepositoryInterface
    ):
        if not isinstance(twitchFollowingStatusRepository, TwitchFollowingStatusRepositoryInterface):
            raise TypeError(f'twitchFollowingStatusRepository argument is malformed: \"{twitchFollowingStatusRepository}\"')
        elif not isinstance(twitchTokensRepository, TwitchTokensRepositoryInterface):
            raise TypeError(f'twitchTokensRepository argument is malformed: \"{twitchTokensRepository}\"')

        self.__twitchFollowingStatusRepository: TwitchFollowingStatusRepositoryInterface = twitchFollowingStatusRepository
        self.__twitchTokensRepository: TwitchTokensRepositoryInterface = twitchTokensRepository

    async def checkStatus(
        self,
        requiredAccessLevel: AccessLevel,
        twitchMessage: TwitchMessage
    ) -> bool:
        # TODO More checking can be done to allow for restricted access for higher subscription tiers
        # TODO a ranking system to simplify managing access would be helpful to reduce the amount of checks needed
        match requiredAccessLevel:
            case AccessLevel.MODERATOR:
                if not twitchMessage.isAuthorMod:
                    return False
            case AccessLevel.VIP:
                if not twitchMessage.isAuthorVip \
                    and not twitchMessage.isAuthorMod:
                    return False
            case AccessLevel.SUBSCRIBER:
                if not await twitchMessage.isTwitchSubscriber() \
                    and not twitchMessage.isAuthorMod \
                    and not twitchMessage.isAuthorVip:
                    return False
            case AccessLevel.FOLLOWER:
                if not await self.__isFollowing(twitchMessage) \
                    and not await twitchMessage.isTwitchSubscriber() \
                    and not twitchMessage.isAuthorMod \
                    and not twitchMessage.isAuthorVip:
                    return False

        return True

    async def __isFollowing(self, message: TwitchMessage) -> bool:
        if not isinstance(message, TwitchMessage):
            raise TypeError(f'message argument is malformed: \"{message}\"')

        twitchAccessToken = await self.__twitchTokensRepository.getAccessTokenById(
            twitchChannelId = await message.getTwitchChannelId()
        )

        if not utils.isValidStr(twitchAccessToken):
            return False

        return await self.__twitchFollowingStatusRepository.isFollowing(
            twitchAccessToken = twitchAccessToken,
            twitchChannelId = await message.getTwitchChannelId(),
            userId = message.getAuthorId()
        )
