from pathlib import Path
from subprocess import TimeoutExpired
from typing import Tuple
from execution.solution_result import TestCaseResultType
from execution.external_code_runner import ExternalCodeRunner
from problem import Problem


class UserSolutionRunner:
    def __init__(self, external_code_runner: ExternalCodeRunner):
        self._external_code_runnner = external_code_runner                

    def run_solution(self, problem: Problem, solution_path: Path) -> Tuple[TestCaseResultType, str]:
        test_case_number = 0
        for test_case_input, correct_output in zip(problem.inputs, problem.outputs):
            test_case_number += 1

            try:
                solution_output = self._external_code_runnner.run(solution_path, test_case_input)
            except TimeoutExpired:
                yield TestCaseResultType.TimeLimitExceeded, f'Time limit exceeded for test case #: {test_case_number}'

            solution_lines = solution_output.strip().splitlines()
            correct_lines = correct_output.strip().splitlines()            

            for correct_line, solution_line in zip(correct_lines, solution_lines):
                if correct_line.strip() != solution_line.strip():
                    yield TestCaseResultType.IncorrectResult, f'Incorrect result on test case #: {test_case_number}'

            yield TestCaseResultType.CorrectResult, ''          
