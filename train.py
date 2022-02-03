import argparse

from env import LapinEnv
from stable_baselines3 import PPO

parser = argparse.ArgumentParser()
parser.add_argument("--tensorboard_logdir", type=str, default="tensorboard", help="Logging directory for tensorboard output")
parser.add_argument("--total_timesteps", type=int, default=10000, help="Number of timesteps to train for")
parser.add_argument("--verbose", type=int, default=1, choices=[0, 1], help="0 to hide training logs, 1 to output training logs")
opts = parser.parse_args()

env = LapinEnv()
model = PPO("MlpPolicy", env, verbose=opts.verbose, tensorboard_log=opts.tensorboard_logdir)
model.learn(total_timesteps=opts.total_timesteps)
env.close()

model.save("ppo_naive")