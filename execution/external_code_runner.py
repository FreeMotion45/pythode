from multiprocessing import Process
from pathlib import Path
from typing import Optional, TextIO, Tuple

from psutil import Popen

from execution.solution_result import SolutionResult


class ExternalCodeRunner:
    def run(self, filepath: Path, input: bytes) -> Tuple[SolutionResult, str]:
        input_stream = TextIO(input)
        output_stream = TextIO()

        external_code_process: Optional[Process] = None
        if filepath.suffix == '.py':
            external_code_process = Popen(['python', str(filepath)], stdin=input_stream, stdout=output_stream)
        
        if external_code_process:
            try:
                external_code_process.wait(timeout=5)
                output_stream.seek(0)
                return output_stream.read()
            except TimeoutError:
                external_code_process.kill()
                raise

        raise ValueError('Currently only supporting Python 3.8 solutions')
