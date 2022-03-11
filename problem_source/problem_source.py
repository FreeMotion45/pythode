from abc import ABC, abstractmethod
from typing import Iterable, List

from problem import Problem


class ProblemSource(ABC):
    @abstractmethod
    def get_problem_list(self) -> List[Problem]:
        ...

    @abstractmethod
    def get_problem_statement(self, problem_identifier: str) -> str:
        ...

    @abstractmethod
    def get_problem_input(self, problem_identifier: str, input_number: int) -> str:
        ...

    @abstractmethod
    def get_problem_output(self, problem_identifier: str, output_number: int) -> str:
        ...

    @abstractmethod
    def get_problem_inputs(self, problem_identifier: str) -> Iterable[str]:
        ...

    @abstractmethod
    def get_problem_outputs(self, problem_identifier: str) -> Iterable[str]:
        ...
