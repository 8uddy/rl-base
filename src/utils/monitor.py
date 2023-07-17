import matplotlib.pyplot as plt

class TrainingMonitor:
    def __init__(self):
        self.rewards_per_episode = []
        self.loss_per_episode = []
        self.steps_per_episode = []

    def record(self, reward, loss, steps):
        self.rewards_per_episode.append(reward)
        self.loss_per_episode.append(loss)
        self.steps_per_episode.append(steps)

    def display(self):
        plt.figure(figsize=(20,5))

        plt.subplot(1,3,1)
        plt.plot(self.rewards_per_episode, label='Reward per episode')
        plt.legend()

        plt.subplot(1,3,2)
        plt.plot(self.loss_per_episode, label='Loss per episode')
        plt.legend()

        plt.subplot(1,3,3)
        plt.plot(self.steps_per_episode, label='Steps per episode')
        plt.legend()

        plt.show()
