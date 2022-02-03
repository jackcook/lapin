import psutil
import threading
import numpy as np
import gym
import subprocess
import time
from victims import WebServerVictim
from tqdm import trange

class LapinEnv(gym.Env):

    def __init__(self):
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Discrete(100)
        #self.observation_space = gym.spaces.Box(low=0, high=100, shape=(1,), dtype=np.float32)
        self.victim = WebServerVictim()
        self.workers = []
        self.last_val = 0

    def get_state(self):
        return len(self.workers)
        #return (len(self.workers),)

    def step(self, action):
        if action == 0:
            # Do nothing
            pass
        if action == 1:
            # Start new worker
            self.workers.append(subprocess.Popen(["python", "mindless_worker.py"]))
        elif action == 2:
            # Kill worker
            if len(self.workers) > 0:
                self.workers.pop().kill()

        #self.victim.start()
        #time.sleep(5)
        #self.victim.stop()

        tail_latency = max(1.5, 5 * np.random.randn() + len(self.workers) / 2)
        cpu_util = psutil.cpu_percent()
        #tail_latency = self.victim.get_data()["percentiles"]["99.9"]

        reward = -1 if cpu_util < 25 else 0
        done = reward == 0

        #print(action, state, f"{tail_latency:.2f}", done)

        return self.get_state(), reward, done, {}

    def close(self):
        for w in self.workers:
            w.kill()

    def reset(self):
        for w in self.workers:
            w.kill()

        self.workers = []

        return self.get_state()
    
    def render(self):
        pass
