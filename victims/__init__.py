from enum import Enum

from .web_server import WebServerVictim

class Victim(Enum):
    WEB_SERVER = WebServerVictim

    def __str__(self):
        return self.name.lower()