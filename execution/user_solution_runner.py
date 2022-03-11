from pathlib import Path
from typing import Tuple
from execution.solution_result import SolutionResultType
from external_code_runner import ExternalCodeRunner
from problem import Problem


class UserSolutionRunner:
    def __init__(self, external_code_runner: ExternalCodeRunner) -> None:
        self._external_code_runnner = external_code_runner

    def run_solution(self, problem: Problem, solution_path: Path) -> Tuple[SolutionResultType, str]:
        test_case_number = 0
        for input, correct_output in zip(input, problem.outputs):
            test_case_number += 1

            try:
                solution_output = self._external_code_runnner.run(solution_path,)
            except TimeoutError:
                return SolutionResultType.RuntimeException, ''

            solution_lines = solution_output.strip().splitlines()
            correct_lines = correct_output.strip().splitlines()            

            for correct_line, solution_line in zip(correct_lines, solution_lines):
                if correct_line.strip() != solution_line.strip():
                    return SolutionResultType.IncorrectResult, f'Incorrect result on test case {test_case_number}'

        return SolutionResultType.CorrectResult, ''
