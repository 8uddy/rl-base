import random

class Environment:
    def __init__(self, size=5):
        self.size = size
        self.reset()

    def reset(self):
        self.agent_position = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        self.passenger_position = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        self.destination_position = (random.randint(0, self.size-1), random.randint(0, self.size-1))
        self.passenger_in_taxi = False
        return self.get_state()

    def get_state(self):
        return self.agent_position, self.passenger_position, self.destination_position, self.passenger_in_taxi

    def step(self, action):
        x, y = self.agent_position

        if action == 'N':
            x = max(0, x - 1)
        elif action == 'S':
            x = min(self.size - 1, x + 1)
        elif action == 'E':
            y = min(self.size - 1, y + 1)
        elif action == 'W':
            y = max(0, y - 1)
        elif action == 'P':
            if self.agent_position == self.passenger_position:
                self.passenger_in_taxi = True
                self.passenger_position = None
        elif action == 'D':
            if self.agent_position == self.destination_position and self.passenger_in_taxi:
                self.passenger_in_taxi = False
                self.destination_position = None

        self.agent_position = (x, y)

        reward = -1  # Default reward is -1 for each step

        if action == 'P' and self.passenger_in_taxi:
            reward += 10  # Picked up the passenger
        elif action == 'D' and self.destination_position is None:
            reward += 20  # Dropped off the passenger
        elif action in ['P', 'D']:
            reward -= 10  # Unsuccessful pick-up or drop-off

        return self.agent_position, reward, self.destination_position is None