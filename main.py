from src.agents.dqn_agent import DQNAgent
from src.monitor import TrainingMonitor
from src.environment import YourEnvironment
from src.config import Config

def main():
    # Initialize the environment and the agent
    env = YourEnvironment()
    config = Config()
    agent = DQNAgent(env.action_space, env.state_space, config.learning_rate, config.discount_factor, config.epsilon)

    # Initialize the monitor
    monitor = TrainingMonitor()

    # Number of episodes for training
    num_episodes = 1000

    for i_episode in range(num_episodes):
        # Reset the environment and get the initial state
        state = env.reset()

        done = False
        total_reward = 0
        steps = 0

        while not done:
            # Select an action
            action = agent.select_action(state)

            # Perform the action and get the reward and the next state
            next_state, reward, done = env.step(action)

            # Update the agent
            agent.update(state, action, reward, next_state, done)

            # Update the total reward and the state
            total_reward += reward
            state = next_state
            steps += 1

        # Record the performance for this episode
        monitor.record(total_reward, agent.loss, steps)

    # Display the training performance
    monitor.display()

if __name__ == "__main__":
    main()
