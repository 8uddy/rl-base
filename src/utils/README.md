TensorBoard-Integration
Wir verwenden TensorBoard für die Protokollierung und Visualisierung von Metriken während des Trainings. Hier ist eine grundlegende Anleitung, wie Sie TensorBoard in unserem Projekt verwenden können:

Installation
Stellen Sie sicher, dass Sie TensorBoard installiert haben. Sie können es mit pip installieren:

```shell
pip install tensorboard
```
Logger-Implementierung
Wir haben eine TensorBoardLogger-Klasse implementiert, die die TensorBoard SummaryWriter-Klasse verwendet:

```python
from torch.utils.tensorboard import SummaryWriter

class TensorBoardLogger:
    def __init__(self, log_dir):
        self.writer = SummaryWriter(log_dir)

    def log_scalar(self, tag, value, step):
        self.writer.add_scalar(tag, value, step)

    def log_histogram(self, tag, values, step):
        self.writer.add_histogram(tag, values, step)

    def log_text(self, tag, text, step):
        self.writer.add_text(tag, text, step)

    def close(self):
        self.writer.close()
Logger-Nutzung
Verwenden Sie den TensorBoardLogger in Ihren Trainingsskripten. Sie können den Logger zu Beginn des Trainings initialisieren und dann die log_scalar, log_histogram und log_text Methoden verwenden, um Metriken, Histogramme und Texte während des Trainings zu protokollieren:

python
Copy code
from src.utils.tensorboard_logger import TensorBoardLogger

# Initialize the logger
logger = TensorBoardLogger(log_dir='runs/experiment1')

for i_episode in range(num_episodes):
    # ...
    # Compute your metrics
    reward = ...
    action_distribution = ...

    # Log the metrics
    logger.log_scalar('Reward', reward, i_episode)
    logger.log_histogram('Action distribution', action_distribution, i_episode)
    logger.log_text('Episode Summary', 'In this episode, the reward was ' + str(reward), i_episode)

# Don't forget to close the logger at the end of training
logger.close()
```

TensorBoard starten
Starten Sie TensorBoard in Ihrem Terminal, um die protokollierten Metriken, Histogramme und Texte zu betrachten:

```shell
tensorboard --logdir runs
```
Dann können Sie TensorBoard in Ihrem Webbrowser öffnen, indem Sie zu der URL gehen, die in Ihrem Terminal angegeben ist (normalerweise http://localhost:6006/).

Mehrere Trainingsläufe vergleichen
Sie können die log_dir-Parameter verwenden, um die Daten von verschiedenen Trainingsläufen in unterschiedlichen Ordnern zu speichern. Auf diese Weise können Sie leicht mehrere Läufe in TensorBoard vergleichen:

```python
# Run 1
logger = TensorBoardLogger(log_dir='runs/experiment1')
# ...

# Run 2
logger = TensorBoardLogger(log_dir='runs/experiment2')
# ...

```
Wenn Sie nun TensorBoard starten, sehen Sie die Daten von beiden Läufen und können sie direkt vergleichen.

Um die oben genannten Anpassungen in Ihr Projekt zu integrieren, fügen Sie die log_histogram-Methode zu Ihrer TensorBoardLogger-Klasse hinzu und aktualisieren Sie Ihre Trainingsskripte, um diese neue Funktion zu nutzen. Denken Sie daran, die entsprechenden Metriken zu berechnen, die Sie als Histogramme darstellen möchten. In diesem Beispiel habe ich action_distribution verwendet, aber Sie können dies an Ihre spezifischen Bedürfnisse anpassen