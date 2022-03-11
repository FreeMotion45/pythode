from abc import ABC, abstractmethod
import os
from secrets import choice
from typing import Callable, Mapping


class CliMenu(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._running = True
        self._options: Mapping[str, Callable] = dict()

    def main_loop(self):
        self._print_menu()
        while self._running:
            choice = self._get_input()
            command = self._get_option(choice)
            command()

    def _stop(self):
        self._running = False

    @abstractmethod
    def _print_menu(self):
        ...

    def _print_options(self):
        for i, option in enumerate(self._options):
            print(f'{i + 1}. {option}')
    
    def _get_option(self, choice: str):
        return self._options[choice]

    def _is_valid_choice(self, choice: str):
        if choice in self._options:
            return True

        if choice.isnumeric() and int(choice) in range(1, len(self._options) + 1):
            return True

        return False

    def _get_input(self):
        choice = input()            
        while not self._is_valid_choice(choice):
            choice = input()

        # Translating choice to the text's equal
        if choice.isnumeric():
            choice = int(choice)
            choice = list(self._options)[choice - 1]

        return choice    