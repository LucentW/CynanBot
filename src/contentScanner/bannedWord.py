from dataclasses import dataclass
from typing import Any

from .absBannedWord import AbsBannedWord
from .bannedWordType import BannedWordType


@dataclass(frozen = True)
class BannedWord(AbsBannedWord):
    word: str

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BannedWord):
            return False

        return self.word.casefold() == other.word.casefold()

    def __hash__(self) -> int:
        return hash((self.word.casefold(), self.wordType))

    @property
    def wordType(self) -> BannedWordType:
        return BannedWordType.EXACT_WORD
