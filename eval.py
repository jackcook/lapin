import numpy as np
import random
from env import LapinEnv

from stable_baselines3 import PPO

env = LapinEnv()
model = PPO.load("ppo_naive")

obs = env.reset()
print(obs)

for i in range(10):
	action, _states = model.predict(obs)
	print(action)
	obs, reward, dones, info = env.step(action)
	# env.render()

env.close()
