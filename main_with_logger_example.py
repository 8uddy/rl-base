from src.utils.tensorboard_logger import TensorBoardLogger

# Initialize the logger
logger = TensorBoardLogger(log_dir='runs/experiment1')

for i_episode in range(num_episodes):
    # ...
    # Compute your metrics
    reward = ...

    # Log the metrics
    logger.log_scalar('Reward', reward, i_episode)

# Don't forget to close the logger at the end of training
logger.close()
