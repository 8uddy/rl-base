from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class DQNetwork:
    def __init__(self, action_space, state_space, learning_rate):
        self.action_space = action_space
        self.state_space = state_space
        self.learning_rate = learning_rate

        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()

        # Adjust the architecture as needed
        model.add(Dense(24, input_dim=self.state_space, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_space, activation='linear'))

        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def predict(self, state):
        return self.model.predict(state)

    def update(self, state, q_values):
        self.model.fit(state, q_values, verbose=0)
