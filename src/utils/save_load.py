#import torch
import yaml

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def save_model(agent, filename):
    """
    Speichern des Modells eines Agenten auf die Festplatte.
    """
    #torch.save(agent.model.state_dict(), filename)

def load_model(agent, filename):
    """
    Laden des Modells eines Agenten von der Festplatte.
    """
    #agent.model.load_state_dict(torch.load(filename))
    #agent.model.eval()  # Setzt das Modell in den Evaluierungsmodus
