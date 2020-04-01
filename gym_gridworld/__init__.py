from gym.envs.registration import registry, register, make, spec

register(
    id='GridWorld-v0',
    entry_point='gym_gridworld.envs:GridWorldEnv',
    kwargs={'map_name' : '4x4', 
    'is_slippery' : False},
    max_episode_steps=200,
    reward_threshold=1.0,
)

register(
    id='GridWorld-slippery-v0',
    entry_point='gym_gridworld.envs:GridWorldEnv',
    kwargs={'map_name' : '4x4',
    'is_slippery' : True},
    max_episode_steps=200,
    reward_threshold=1.0,
)


register(
    id='GridWorld-3x3-Wall-v0',
    entry_point='gym_gridworld.envs:GridWorldEnv',
    kwargs={'map_name' : '3x3_WALL', 
    'is_slippery' : False},
    max_episode_steps=200,
    reward_threshold=1.0,
)

register(
    id='GridWorld-5x5-AB-v0',
    entry_point='gym_gridworld.envs:GridWorldEnv',
    kwargs={'map_name' : '5x5_AB', 
    'is_slippery' : False},
    max_episode_steps=200,
    reward_threshold=1.0,
)

# register(
#     id='GridWorld-v0',
#     entry_point='gym.envs.toy_text:FrozenLakeEnv',
#     kwargs={'map_name' : '4x4_noHoles'},
#     max_episode_steps=200,
#     reward_threshold=0.78, # optimum = .8196
# )

# register(
#     id='Copy-v0',
#     entry_point='gym.envs.algorithmic:CopyEnv',
#     max_episode_steps=200,
#     reward_threshold=25.0,
# )