from abc import ABC, abstractmethod

from frozendict import frozendict

from ..absCheerAction import AbsCheerAction
from ...twitch.configuration.twitchChannelProvider import TwitchChannelProvider
from ...users.userInterface import UserInterface


class BeanChanceCheerActionHelperInterface(ABC):

    @abstractmethod
    async def handleBeanChanceCheerAction(
        self,
        actions: frozendict[int, AbsCheerAction],
        bits: int,
        broadcasterUserId: str,
        cheerUserId: str,
        cheerUserName: str,
        message: str,
        moderatorTwitchAccessToken: str,
        moderatorUserId: str,
        twitchChatMessageId: str | None,
        userTwitchAccessToken: str,
        user: UserInterface
    ) -> bool:
        pass

    @abstractmethod
    def setTwitchChannelProvider(self, provider: TwitchChannelProvider | None):
        pass
