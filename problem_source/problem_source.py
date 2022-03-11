from abc import ABC, abstractmethod
from typing import Iterable

from problem import Problem


class ProblemSource(ABC):
    @abstractmethod
    def get_problem_statement(self, problem_identifier: str) -> str:
        ...

    @abstractmethod
    def get_problem_inputs(self, problem_identifier: str) -> Iterable[str]:
        ...

    @abstractmethod
    def get_problem_outputs(self, problem_identifier: str) -> Iterable[str]:
        ...
