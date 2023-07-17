from src.agents.dqn_agent import DQNAgent
from src.monitor import TrainingMonitor
from src.environment import YourEnvironment
from src.utils.load_save import load_config


def hyperparameter_tuning(config_path):
    # Load the configuration file
    config = load_config(config_path)

    # Initialize the environment
    env = YourEnvironment()

    # Get the hyperparameters to tune from the config
    learning_rates = config['hyperparameters']['learning_rates']
    discount_factors = config['hyperparameters']['discount_factors']
    epsilons = config['hyperparameters']['epsilons']

    # Get number of episodes from config
    num_episodes = config['experiment']['num_episodes']

    # Initialize the best score and the best hyperparameters
    best_score = -float('inf')
    best_hyperparameters = None

    # Try all combinations of hyperparameters
    for learning_rate in learning_rates:
        for discount_factor in discount_factors:
            for epsilon in epsilons:
                # Initialize the agent with the current hyperparameters
                agent = DQNAgent(env.action_space, env.state_space, learning_rate, discount_factor, epsilon)

                # Initialize the monitor
                monitor = TrainingMonitor()

                # Train the agent (you could also define a separate function for the training loop)
                for i_episode in range(num_episodes):
                # (same training loop as in the train.py file...)

                # Compute the average reward
                average_reward = sum(monitor.rewards_per_episode) / num_episodes

                # If this is the best score so far, save the score and the hyperparameters
                if average_reward > best_score:
                    best_score = average_reward
                    best_hyperparameters = (learning_rate, discount_factor, epsilon)

    print(f'Best score: {best_score}')
    print(f'Best hyperparameters: {best_hyperparameters}')


if __name__ == "__main__":
    hyperparameter_tuning('configs/dqn_config.yaml')
