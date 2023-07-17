from multiprocessing import Pool
from src.utils.load_save import load_config

def train_one(config):
    # Extract hyperparameters from config
    learning_rate = config['agent']['learning_rate']
    discount_factor = config['agent']['discount_factor']
    epsilon = config['agent']['epsilon']

    # Initialize the environment
    env = YourEnvironment()

    # Initialize the agent with the current hyperparameters
    agent = DQNAgent(env.action_space, env.state_space, learning_rate, discount_factor, epsilon)

    # Initialize the monitor
    monitor = TrainingMonitor()

    # Train the agent
    for i_episode in range(num_episodes):
        # (same training loop as in the train.py file...)

    # Compute the average reward
    average_reward = sum(monitor.rewards_per_episode) / num_episodes
    return average_reward, (learning_rate, discount_factor, epsilon)

def hyperparameter_tuning(config_path):
    # Load the configuration file
    config = load_config(config_path)

    # Define a list of configs for each training run
    configs = []

    # Try all combinations of hyperparameters
    for learning_rate in config['hyperparameters']['learning_rates']:
        for discount_factor in config['hyperparameters']['discount_factors']:
            for epsilon in config['hyperparameters']['epsilons']:
                # Prepare the config for this run
                run_config = config.copy()
                run_config['agent']['learning_rate'] = learning_rate
                run_config['agent']['discount_factor'] = discount_factor
                run_config['agent']['epsilon'] = epsilon
                configs.append(run_config)

    # Use a pool of workers to run trainings in parallel
    with Pool() as p:
        results = p.map(train_one, configs)

    # Find the best result
    best_score, best_hyperparameters = max(results, key=lambda x: x[0])

    print(f'Best score: {best_score}')
    print(f'Best hyperparameters: {best_hyperparameters}')

if __name__ == "__main__":
    hyperparameter_tuning('configs/dqn_config.yaml')
