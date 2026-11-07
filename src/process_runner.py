import os
import subprocess
import threading
from typing import Callable, Optional, List


class ProcessRunner:
    """Gère l'exécution d'un processus en arrière-plan avec redirection des sorties."""

    def __init__(self, on_output: Optional[Callable[[str], None]] = None,
                 on_finished: Optional[Callable[[int], None]] = None):
        self.on_output = on_output
        self.on_finished = on_finished
        self.process: Optional[subprocess.Popen] = None
        self._thread: Optional[threading.Thread] = None
        self.is_running: bool = False

    def run(self, command: List[str], cwd: Optional[str] = None):
        """Lance une commande en tâche de fond."""
        if self.is_running:
            raise RuntimeError("Un processus est déjà en cours d'exécution.")

        self.is_running = True
        self._thread = threading.Thread(target=self._worker, args=(command, cwd), daemon=True)
        self._thread.start()

    def _worker(self, command: List[str], cwd: Optional[str]):
        try:
            self.process = subprocess.Popen(
                command,
                cwd=cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            # Lecture ligne par ligne en streaming
            for line in iter(self.process.stdout.readline, ''):
                if self.on_output:
                    self.on_output(line)

            self.process.stdout.close()
            return_code = self.process.wait()

        except Exception as e:
            if self.on_output:
                self.on_output(f"\n[ERREUR D'EXÉCUTION] {str(e)}\n")
            return_code = -1
        finally:
            self.is_running = False
            if self.on_finished:
                self.on_finished(return_code)

    def stop(self):
        """Arrête le processus en cours s'il existe."""
        if self.process and self.is_running:
            self.process.terminate()
            self.is_running = False
