from dataclasses import dataclass
from enum import Enum


class SolutionResultType(Enum):
    TimeLimitExceeded = 1
    IncorrectResult = 2
    RuntimeException = 3
    CorrectResult = 4
    