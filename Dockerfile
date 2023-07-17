# Basierend auf dem offiziellen Python-Image
FROM python:3.8-slim-buster

# Setzen Sie das Arbeitsverzeichnis im Container auf /app
WORKDIR /app

# Kopieren Sie die Projektdateien in den Container
COPY . .

# Installieren Sie die Projektanforderungen
RUN pip install --no-cache-dir -r requirements.txt

# Setzen Sie die Umgebungsvariable für Python, um stdout und stderr zu puffern.
ENV PYTHONUNBUFFERED=1

# Führen Sie das Haupttrainingsskript aus, wenn der Container gestartet wird
CMD ["python", "main.py"]
