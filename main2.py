import numpy as np
import random
from env import LapinEnv

from stable_baselines3 import PPO

env = LapinEnv()
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="tensorboard")
model.learn(total_timesteps=1000)
env.close()

model.save("ppo_naive")

# del model
# model = PPO.load("ppo_naive")
# 
# obs = env.reset()
# print(obs)
# 
# for i in range(10):
# 	action, _states = model.predict(obs)
# 	print(action)
# 	obs, reward, dones, info = env.step(action)
# 	# env.render()
# 
# env.close()
