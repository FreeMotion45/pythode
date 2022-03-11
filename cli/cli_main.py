from pathlib import Path

from problem_source.file_system_data_source import FileSystemDataSource

from cli.main_menu import MainMenu


def run_cli():
    problems_root_dir = Path(__file__).parent.parent / 'problems'
    main_menu = MainMenu(FileSystemDataSource(problems_root_dir))
    main_menu.main_loop()
