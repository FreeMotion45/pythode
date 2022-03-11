from abc import ABC, abstractmethod

from problem import Problem


class ProblemSource(ABC):
    @abstractmethod
    def get_problem(problem_identifier: str) -> Problem:
        ...
    