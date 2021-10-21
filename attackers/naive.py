import subprocess

class NaiveAttacker:

    def __init__(self):
        self.naive_procs = []

    def start(self):
        for _ in range(100):
            self.naive_procs.append(subprocess.Popen(["python", "attackers/naive_runner.py"]))

    def stop(self):
        for p in self.naive_procs:
            p.kill()