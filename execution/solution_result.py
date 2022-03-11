from dataclasses import dataclass
from enum import Enum


class TestCaseResultType(Enum):
    TimeLimitExceeded = 'Time limit exceeded'
    IncorrectResult = 'Incorrect result'
    RuntimeException = 'Runtime exception'
    CorrectResult = 'Correct result'
