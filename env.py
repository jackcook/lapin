import gym
import psutil
import subprocess

class LapinEnv(gym.Env):

    def __init__(self):
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Discrete(100)
        self.workers = []
        self.last_val = 0

    def get_state(self):
        return len(self.workers)

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

        cpu_util = psutil.cpu_percent()
        reward = None
        
        if cpu_util > self.last_val:
            reward = 1
        elif cpu_util == self.last_val:
            reward = 0
        else:
            reward = -1
        
        self.last_val = cpu_util

        done = cpu_util >= 95
        info = {}

        return self.get_state(), reward, done, info

    def close(self):
        for w in self.workers:
            w.kill()

    def reset(self):
        for w in self.workers:
            w.kill()

        self.workers = []
        self.last_val = 0

        return self.get_state()

    def render(self):
        pass
