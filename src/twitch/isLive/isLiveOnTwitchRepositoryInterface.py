from abc import ABC, abstractmethod

from frozendict import frozendict

from ...misc.clearable import Clearable


class IsLiveOnTwitchRepositoryInterface(Clearable, ABC):

    @abstractmethod
    async def areLive(self, twitchChannelIds: set[str]) -> frozendict[str, bool]:
        pass

    @abstractmethod
    async def isLive(self, twitchChannelId: str) -> bool:
        pass
