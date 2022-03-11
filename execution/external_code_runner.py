from io import StringIO
from multiprocessing import Process
from pathlib import Path
from typing import Optional

from subprocess import PIPE, Popen, TimeoutExpired


class ExternalCodeRunner:
    def run(self, filepath: Path, test_case_input: str) -> str:
        external_code_process: Optional[Popen] = None
        if filepath.suffix == '.py':
            external_code_process: Popen = Popen(['python', str(filepath)], stdin=PIPE, stdout=PIPE)
        
        if external_code_process:
            try:                
                stdin = test_case_input.encode('ascii')
                process_output, stderr = external_code_process.communicate(input=stdin, timeout=5)                            
                return process_output.decode('ascii')
            except TimeoutExpired:
                external_code_process.kill()
                raise

        raise ValueError('Currently only supporting Python 3.8 solutions')
