import argparse
import numpy as np
from gym_duckietown.envs import DuckietownEnv

# declare the arguments
parser = argparse.ArgumentParser()

# Do not change this
parser.add_argument('--max_steps', type=int, default=2000, help='max_steps')

# You should set them to different map name and seed accordingly
parser.add_argument('--map-name', default='map5')
parser.add_argument('--seed', type=int, default=11, help='random seed')
args = parser.parse_args()

env = DuckietownEnv(
    map_name = args.map_name,
    domain_rand = False,
    draw_bbox = False,
    max_steps = args.max_steps,
    seed = args.seed
)

obs = env.reset()
env.render()

total_reward = 0

# please remove this line for your own policy
actions = np.loadtxt('./map5_seed11.txt', delimiter=',')

for (speed, steering) in actions:

    obs, reward, done, info = env.step([speed, steering])
    total_reward += reward
    
    print('Steps = %s, Timestep Reward=%.3f, Total Reward=%.3f' % (env.step_count, reward, total_reward))

    env.render()

print("Total Reward", total_reward)

# dump the controls using numpy
np.savetxt('./map5_seed11.txt', actions, delimiter=',')