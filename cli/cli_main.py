from pathlib import Path
import sys, os
sys.path.append(os.getcwd())

from problem_source.file_system_data_source import FileSystemDataSource

from cli.main_menu import MainMenu


if __name__ == '__main__':
    problems_root_dir = Path(__file__).parent.parent / 'problems'
    main_menu = MainMenu(FileSystemDataSource(problems_root_dir))
    main_menu.main_loop()