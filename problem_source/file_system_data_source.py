from pathlib import Path
from plistlib import InvalidFileException
from typing import Iterable
from problem_source.problem_source import ProblemSource

INPUTS_DIR = 'inputs'
OUTPUTS_DIR = 'outputs'
STATEMENTS_DIR = 'statements'


class FileSystemDataSource(ProblemSource):
    def __init__(self, problems_root_dir: Path, problem_source: ProblemSource) -> None:
        super().__init__()
        self._root_dir = problems_root_dir
        self._inputs_dir = problems_root_dir / INPUTS_DIR
        self._outputs_dir = problems_root_dir / OUTPUTS_DIR
        self._statement_dir = problems_root_dir / STATEMENTS_DIR

    def get_problem_statement(self, problem_identifier: str) -> str:
        problem_statement = self._statement_dir / problem_identifier
        if not problem_statement.is_file():
            raise InvalidFileException(message=f'{problem_identifier} is missing it\'s statement file!')
        
        return problem_statement.read_text()

    def get_problem_inputs(self, problem_identifier: str) -> Iterable[str]:
        problem_inputs_dir = self._inputs_dir / problem_identifier
        if not problem_inputs_dir.is_dir():
            raise InvalidFileException(message=f'{problem_identifier} is missing an inputs directory!')

        for inputs_path in problem_inputs_dir.iterdir():
            yield inputs_path.read_text()

    def get_problem_outputs(self, problem_identifier: str) -> Iterable[str]:
        problem_outputs_dir = self._inputs_dir / self._outputs_dir
        if not problem_outputs_dir.is_dir():
            raise InvalidFileException(message=f'{problem_identifier} is missing an outputs directory!')

        for outputs_path in problem_outputs_dir.iterdir():
            yield outputs_path.read_text()

    