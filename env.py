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
		self.observation_space = gym.spaces.Box(low=0, high=100, shape=(1,), dtype=np.float32)
		self.victim = WebServerVictim()
		self.workers = []
		self.last_val = 0

	def step(self, action):
		if action == 0:
			# Do nothing
			pass
		if action == 1:
			# Start new worker
			for i in range(5):
				self.workers.append(subprocess.Popen(["python", "mindless_worker.py"]))
		elif action == 2:
			# Kill worker
			for i in range(5):
				if len(self.workers) > 0:
					self.workers.pop().kill()

		self.victim.start()
		time.sleep(5)
		self.victim.stop()

		state = len(self.workers)
		# print(self.victim.get_data())
		reward = self.victim.get_data()["percentiles"]["99.9"] - self.last_val
		self.last_val = self.victim.get_data()["percentiles"]["99.9"]

		done = self.last_val > 5
		info = {}

		print(action, state, f"{reward:.2f}", done)

		return (state,), reward, done, info

	def reset(self):
		for w in self.workers:
			w.kill()

		self.workers = []
		self.last_val = 0
		state = len(self.workers)

		return (state,)
	
	def render(self):
		pass