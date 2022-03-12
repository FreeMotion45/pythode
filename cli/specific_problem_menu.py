import os
from pathlib import Path
from typing import Iterable, Tuple
from cli.cli_menu import CliMenu
from execution.solution_result import TestCaseResultType
from execution.user_solution_runner import UserSolutionRunner
from problem import Problem

class SpecificProblemMenu(CliMenu):
    def __init__(self, user_solution_runner: UserSolutionRunner, problem: Problem) -> None:
        super().__init__()
        self._solution_runner = user_solution_runner
        self._problem = problem
        self._options['Back'] = self._stop
        self._options['Submit solution'] = self._submit_solution        
        self._options['Rerun last solution file'] = self._submit_last_solution_file
        self._options['See test case'] = self._see_test_case        

        self._last_solution_file = ''

    def _set_last_solution_file(self, solution_file: str):
        self._last_solution_file = solution_file
        while self._last_solution_file[0] in ['"', '\'']:
            self._last_solution_file = self._last_solution_file[1:]
        while self._last_solution_file[-1] in ['"', '\'']:
            self._last_solution_file = self._last_solution_file[:-1]

    def _see_test_case(self):
        print('WARNING:')
        print('Seeing the test cases is bad practice. However, here in Pythode we still allow it.')
        print('Are you sure you want to see a test case?')
        user_input = input('Type the test case number. (N / No / C / Cancel) to cancel. >> ').lower()
        if user_input.isnumeric():
            print(self._problem.get_test_case_input(user_input))
        else:
            print('Test case peek aborted')

    def _submit_last_solution_file(self):        
        if self._last_solution_file == '':
            print('You haven\'t submitted any solution file yet!')
            return        
        solution_results = self._solution_runner.run_solution(self._problem, Path(self._last_solution_file))
        self._print_results(solution_results)

    def _submit_solution(self):
        solution_file = input('Solution file: ')
        self._set_last_solution_file(solution_file)
        print('Running solution...')
        self._submit_last_solution_file()        

    def _print_results(self, solution_results: Iterable[Tuple[TestCaseResultType, str]]):
        all_cases_passed = True        
        counter = 0
        for test_case_result_type, msg in solution_results:
            counter += 1
            print(f'Test case #: {counter}: ... ', end='')
            if test_case_result_type == TestCaseResultType.CorrectResult:
                print('✅')
            else:
                print(test_case_result_type.value, '❌') 
                all_cases_passed = False
                print(msg)
                break

        if all_cases_passed:
            print('Congrats! You have successfully solved the question, well done! 😎')


    def _print_menu(self):
        os.system('cls')
        print(self._problem.statement)
        print()
        self._print_options()