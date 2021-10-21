from enum import Enum

from .do_nothing import DoNothingAttacker
from .naive import NaiveAttacker

class Attacker(Enum):
    DO_NOTHING = DoNothingAttacker
    NAIVE = NaiveAttacker

    def __str__(self):
        return self.name.lower()