import matplotlib.pyplot as plt


from src.agents.taxi_qn_agent import QLearningAgent
from src.enviroment.taxi_env import Environment
from src.utils.tensorboard_logger import TensorBoardLogger


# Initialize the agent and the environment
agent = QLearningAgent(['N', 'S', 'E', 'W', 'P', 'D'])
env = Environment()

# Number of episodes to train the agent
n_episodes = 100
rewards_per_episode = []

for episode in range(n_episodes):
    # Reset the environment and get the initial state
    state = env.reset()
    total_reward = 0
    print(episode)

    while True:
        # The agent chooses an action
        action = agent.choose_action(state)

        # The agent performs the action and gets the reward and new state
        new_state, reward, done = env.step(action)

        # The agent updates the Q-values
        agent.update_q_value(state, action, reward, new_state)

        state = new_state
        total_reward += reward

        if done:
            # The episode ends if the agent has delivered the passenger
            print('done', total_reward )
            break

    rewards_per_episode.append(total_reward)

# Plot the rewards
plt.plot(rewards_per_episode)
plt.title('Total rewards per episode (training)')
plt.xlabel('Episode')
plt.ylabel('Total reward')
plt.show()
