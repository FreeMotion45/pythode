import os
from typing import Callable, Mapping

from cli.cli_menu import CliMenu
from cli.problem_selection_menu import ProblemSelectionMenu
from problem_source.problem_source import ProblemSource


class MainMenu(CliMenu):
    def __init__(self, problem_source: ProblemSource) -> None:
        super().__init__()
        
        self._problem_selection_menu = ProblemSelectionMenu(problem_source)

        self._options['Solve problems'] = self._open_problem_selection_menu            
        self._options['Quit'] = self._stop

    def _open_problem_selection_menu(self):
        os.system('cls')
        self._problem_selection_menu.main_loop()
        
        os.system('cls')
        self._print_menu()

    def _print_menu(self):
        print('Welcome to Pythode!')
        print('This is the BEST platform to use Python')
        print('to solve various algorithmic problems.')
        print('Please select one of the following options:')
        for i, option in enumerate(self._options):
            print(f'{i + 1}. {option}')
