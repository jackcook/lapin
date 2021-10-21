import argparse
import sys
import time

from attackers import Attacker
from victims import Victim

def get_cls(parent, value):
    try:
        return parent[value.upper()]
    except:
        print(f"Invalid {parent.__name__.lower()} type: {value}")
        sys.exit(1)

parser = argparse.ArgumentParser(description="Collect data for Lapin.")
parser.add_argument("-d", "--duration", type=int, default=10, help="Trace duration.")
parser.add_argument("-a", "--attacker", type=lambda a: get_cls(Attacker, a), choices=list(Attacker), default="naive")
parser.add_argument("-v", "--victim", type=lambda v: get_cls(Victim, v), choices=list(Victim), default="web_server")
opts = parser.parse_args()

attacker = opts.attacker.value()
victim = opts.victim.value()

victim.start()
attacker.start()

time.sleep(opts.duration)

victim.stop()
attacker.stop()

print(victim.get_data())