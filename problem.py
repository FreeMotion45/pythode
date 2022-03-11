from ctypes import Union
from typing import Iterable, Optional

from problem_source.problem_source import ProblemSource


class Problem:
    def __init__(self, id: Union[str, int], problem_source: ProblemSource) -> None:
        self._id = id
        self._problem_source = problem_source        

    @property
    def statement(self) -> str:
        return self._problem_source.get_problem_statement(self._id)

    @property
    def inputs(self) -> Iterable[str]:
        return self._problem_source.get_problem_inputs(self._id)

    @property
    def outputs(self) -> Iterable[str]:
        return self._problem_source.get_problem_inputs(self._id)
