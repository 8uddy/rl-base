import numpy as np
import random
from src.agents.base_agent import BaseAgent
from src.networks.dqn_network import DQNetwork


class DQNAgent(BaseAgent):
    def __init__(self, action_space, state_space, learning_rate, discount_factor, epsilon):
        super().__init__(action_space, state_space)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.network = DQNetwork(action_space, state_space, learning_rate)
        self.memory = []

    def select_action(self, state):
        if np.random.rand() < self.epsilon:
            return random.choice(self.action_space)
        else:
            return np.argmax(self.network.predict(state))

    def update(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

        # Here comes the training logic
        # You need to sample experiences from memory and use them to train the network

    def train(self, batch_size):
# Here comes the logic of sampling a batch of experiences from memory
# And using them to update the network
