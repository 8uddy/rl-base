import librosa

def load_audio_file(file_path, sample_rate=22050):
    """
    Laden der Audiodatei mit einer bestimmten Abtastrate.
    """
    audio, _ = librosa.load(file_path, sr=sample_rate)
    return audio

def convert_to_mono(audio):
    """
    Konvertiert die Audiodatei in Mono, indem es die Kanäle zusammenfasst.
    """
    mono_audio = librosa.to_mono(audio)
    return mono_audio

def normalize_audio(audio):
    """
    Normalisiert die Audiodatei, so dass sie eine Amplitude zwischen -1 und 1 hat.
    """
    normalized_audio = librosa.util.normalize(audio)
    return normalized_audio

def extract_features(audio, sample_rate=22050, n_mfcc=13):
    """
    Extrahiert Merkmale aus der Audiodatei, wie Mel-Frequenz-Cepstrum-Koeffizienten (MFCCs).
    """
    mfccs = librosa.feature.mfcc(audio, sr=sample_rate, n_mfcc=n_mfcc)
    return mfccs

def preprocess_audio_file(file_path):
    """
    Vorverarbeitung der Audiodatei: Laden, in Mono konvertieren, normalisieren und Merkmale extrahieren.
    """
    audio = load_audio_file(file_path)
    mono_audio = convert_to_mono(audio)
    normalized_audio = normalize_audio(mono_audio)
    features = extract_features(normalized_audio)

    return features
