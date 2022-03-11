from multiprocessing import Process
from pathlib import Path
from typing import Optional, TextIO

from psutil import Popen


class ExternalCodeRunner:
    def run(filepath: Path, input: bytes) -> str:
        input_stream = TextIO(input)
        output_stream = TextIO()

        external_code_process: Optional[Process] = None
        if filepath.suffix == '.py':
            external_code_process = Popen(['python', str(filepath)], stdin=input_stream, stdout=output_stream)

        if external_code_process:
            try:
                external_code_process.wait(timeout=5)
            except TimeoutError:
                pass

        output_stream.seek(0)
        return output_stream.read()
