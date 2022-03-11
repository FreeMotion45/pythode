from pathlib import Path
from plistlib import InvalidFileException
from typing import Iterable, List
from problem import Problem
from problem_source.problem_source import ProblemSource

INPUTS_DIR = 'inputs'
OUTPUTS_DIR = 'outputs'
STATEMENTS_DIR = 'statements'


class FileSystemDataSource(ProblemSource):
    def __init__(self, problems_root_dir: Path) -> None:
        super().__init__()
        self._inputs_dir = problems_root_dir / INPUTS_DIR
        self._outputs_dir = problems_root_dir / OUTPUTS_DIR
        self._statement_dir = problems_root_dir / STATEMENTS_DIR

    def get_problem_list(self) -> List[Problem]:
        problems = []
        for problem_statement in self._statement_dir.iterdir():
            if problem_statement.is_file():
                file_name = problem_statement.name
                problem_id = file_name.split('-')[0].strip()
                problem_name = file_name[:-len(problem_statement.suffix)]
                problem = Problem(problem_id, problem_name, self)
                problems.append(problem)
        return problems

    def get_problem_statement(self, problem_identifier: str) -> str:
        for problem_file in self._statement_dir.iterdir():
            if problem_file.name.startswith(problem_identifier):
                return problem_file.read_text()
                
        raise InvalidFileException(message=f'{problem_identifier} is missing it\'s statement file!')

    def get_problem_input(self, problem_identifier: str, input_number: int) -> str:
        problem_input_path = self._inputs_dir / problem_identifier / ( str(input_number) + '.txt' )
        if not problem_input_path.is_file():
            raise InvalidFileException(message=f'Can\'t find test case input #: {input_number} for problem {problem_identifier}')
        return problem_input_path.read_text()

    def get_problem_output(self, problem_identifier: str, output_number: int) -> str:
        problem_output_path = self._inputs_dir / problem_identifier / str(output_number) + '.txt'
        if not problem_output_path.is_file():
            raise InvalidFileException(message=f'Can\'t find test case result #: {output_number} for problem {problem_identifier}')
        return problem_output_path.read_text()

    def get_problem_inputs(self, problem_identifier: str) -> Iterable[str]:
        problem_inputs_dir = self._inputs_dir / problem_identifier
        if not problem_inputs_dir.is_dir():
            raise InvalidFileException(message=f'{problem_identifier} is missing an inputs directory!')

        for inputs_path in problem_inputs_dir.iterdir():
            yield inputs_path.read_text()

    def get_problem_outputs(self, problem_identifier: str) -> Iterable[str]:
        problem_outputs_dir = self._outputs_dir / problem_identifier
        if not problem_outputs_dir.is_dir():
            raise InvalidFileException(message=f'{problem_identifier} is missing an outputs directory!')

        for outputs_path in problem_outputs_dir.iterdir():
            yield outputs_path.read_text()
