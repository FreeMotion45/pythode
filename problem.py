from typing import Iterable, Optional, Union


class Problem:
    def __init__(self, id: Union[str, int], name: str, problem_source) -> None:
        self._id = id
        self._name = name
        self._problem_source = problem_source    

    @property
    def id(self) -> str:
        return self._id    

    @property
    def name(self) -> str:
        return self._name

    @property
    def statement(self) -> str:
        return self._problem_source.get_problem_statement(self._id)

    @property
    def inputs(self) -> Iterable[str]:
        return self._problem_source.get_problem_inputs(self._id)

    @property
    def outputs(self) -> Iterable[str]:
        return self._problem_source.get_problem_outputs(self._id)

    def get_test_case_input(self, test_case: int):
        return self._problem_source.get_problem_input(self._id, test_case)
