import abc

class BaseAgent(abc.ABC):
    """
    Eine abstrakte Basisklasse, die die gemeinsame Schnittstelle für alle RL-Agenten definiert.
    """

    def __init__(self, action_space, state_space):
        """
        Initialisiert den Agenten.
        :param action_space: Der Aktionsraum des Agenten.
        :param state_space: Der Zustandsraum des Agenten.
        """
        self.action_space = action_space
        self.state_space = state_space

    @abc.abstractmethod
    def select_action(self, state):
        """
        Wählt eine Aktion basierend auf dem gegebenen Zustand aus.
        :param state: Der aktuelle Zustand der Umgebung.
        :return: Die ausgewählte Aktion.
        """
        pass

    @abc.abstractmethod
    def update(self, state, action, reward, next_state, done):
        """
        Aktualisiert den Agenten basierend auf der Erfahrung (state, action, reward, next_state).
        :param state: Der aktuelle Zustand der Umgebung.
        :param action: Die vom Agenten ausgeführte Aktion.
        :param reward: Die erhaltene Belohnung.
        :param next_state: Der Zustand der Umgebung nach der Ausführung der Aktion.
        :param done: Ein Boolean, der angibt, ob die Episode beendet ist.
        """
        pass
