import subprocess
import requests

class WebServerVictim:

    def __init__(self):
        pass

    def start(self):
        self.server_proc = subprocess.Popen(["python", "victims/web_server_runner.py"], stdout=subprocess.PIPE)
        self.requester_proc = subprocess.Popen(["python", "victims/web_server_requester.py"], stdout=subprocess.PIPE)

    def stop(self):
        self.requester_proc.kill()
        self.data = requests.get("http://localhost:8080/tail_latency").json()
        self.server_proc.kill()

    def get_data(self):
        return self.data