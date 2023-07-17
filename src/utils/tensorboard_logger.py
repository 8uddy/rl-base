from torch.utils.tensorboard import SummaryWriter
import matplotlib.pyplot as plt

def plot_rewards(rewards, title='Training Rewards'):
    plt.figure()
    plt.plot(rewards)
    plt.title(title)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.show()


class TensorBoardLogger:
    def __init__(self, log_dir):
        self.writer = SummaryWriter(log_dir)

    def log_scalar(self, tag, value, step):
        self.writer.add_scalar(tag, value, step)

    def close(self):
        self.writer.close()
