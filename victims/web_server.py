import subprocess
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class WebServerVictim:

    def __init__(self):
        pass

    def start(self):
        self.server_proc = subprocess.Popen(["python", "victims/web_server_runner.py"], stdout=subprocess.PIPE)
        self.requester_proc = subprocess.Popen(["python", "victims/web_server_requester.py"], stdout=subprocess.PIPE)

    def stop(self):
        self.requester_proc.kill()
        
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        # session.mount('https://', adapter)
        
        url = "http://localhost:8080/tail_latency"
        self.data = session.get(url).json()
        # self.data = requests.get("http://localhost:8080/tail_latency").json()
        self.server_proc.kill()

    def get_data(self):
        return self.data