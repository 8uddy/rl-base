import numpy as np
from src.agents.base_agent import BaseAgent

class QLearningAgent():
    def __init__(self, actions, learning_rate=0.01, discount_factor=0.99, exploration_rate=0.1):
        self.actions = actions
        self.lr = learning_rate
        self.df = discount_factor
        self.er = exploration_rate
        self.q_table = {}

    def choose_action(self, state):
        if np.random.uniform() < self.er:
            # Explore: choose a random action
            return np.random.choice(self.actions)
        else:
            # Exploit: choose the action with the highest expected future reward
            state = tuple(state)
            q_values = [self.get_q_value(state, action) for action in self.actions]
            return self.actions[np.argmax(q_values)]

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        state = tuple(state)
        next_state = tuple(next_state)

        old_q_value = self.get_q_value(state, action)
        max_next_q_value = max([self.get_q_value(next_state, a) for a in self.actions])

        # Q-learning update rule
        new_q_value = old_q_value + self.lr * (reward + self.df * max_next_q_value - old_q_value)
        self.q_table[(state, action)] = new_q_value
