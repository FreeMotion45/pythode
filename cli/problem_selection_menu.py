import os
from cli.cli_menu import CliMenu
from cli.specific_problem_menu import SpecificProblemMenu
from execution.external_code_runner import ExternalCodeRunner
from execution.user_solution_runner import UserSolutionRunner
from problem import Problem
from problem_source.problem_source import ProblemSource


class ProblemSelectionMenu(CliMenu):
    def __init__(self, problem_source: ProblemSource) -> None:
        super().__init__()

        external_code_runner = ExternalCodeRunner()
        self._user_solution_runner = UserSolutionRunner(external_code_runner)

        self._problem_source = problem_source
        self._problem_list = problem_source.get_problem_list()    

        self._options['Back'] = self._stop
        for problem in self._problem_list:
            self._options[problem.id] = self._select_problem
        
        self._current_problem_id = ''

    def _get_option(self, choice: str):
        if choice.isnumeric():
            choice = int(choice) - 2  # - 2 because 1 is reserved for back and also 1 indexed.
            chosen_problem: Problem = self._problem_list[choice]
            choice = chosen_problem.id
            
        self._current_problem_id = choice        
        return super()._get_option(choice)

    def _select_problem(self):
        problem = [problem for problem in self._problem_list if problem.id == self._current_problem_id][0]
        specific_problem_menu = SpecificProblemMenu(self._user_solution_runner, problem)
        specific_problem_menu.main_loop()

        os.system('cls')
        self._print_menu()

    def _back(self):
        self._running = False

    def _print_menu(self):
        print('Select a problem to solve (1A, 4B...)')
        for i, problem in enumerate(self._problem_list):
            print(f'{i + 2}. {problem.name}')
        print()
        print('Type `1` or `Back` to go back.')
