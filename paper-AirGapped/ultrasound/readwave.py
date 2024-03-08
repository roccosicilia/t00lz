
import numpy as np
import wave

# Definisci le frequenze di soglia e le durate minime
thresholds = [(9900, 11000, 0), (19900, 20100, 1)]
min_duration = 0.7

# Carica il file audio WAV
audio_file = "Registrazione-1.wav"
wav = wave.open(audio_file, 'rb')
sample_width = wav.getsampwidth()
frame_rate = wav.getframerate()
n_frames = wav.getnframes()

# Leggi i dati audio
audio_signal = np.frombuffer(wav.readframes(n_frames), dtype=np.int16)

# Calcola la trasformata di Fourier
frequencies, amplitudes = np.fft.fft(audio_signal), np.fft.fftshift(audio_signal)

# Calcola le frequenze corrispondenti alle posizioni nella trasformata di Fourier
frequencies = np.fft.fftfreq(len(frequencies), 1 / frame_rate)

# Inizializza una variabile per tenere traccia dell'output
output = ""

# Trova i picchi per ciascun intervallo di frequenza
for lower_threshold, upper_threshold, symbol in thresholds:
    within_range_indices = np.where((frequencies >= upper_threshold) & (frequencies <= lower_threshold))[0]
    
    # Trova i segmenti temporali nell'intervallo desiderato con una durata maggiore della soglia minima
    within_range_segments = []
    segment_start = None
    
    for index in within_range_indices:
        if segment_start is None:
            segment_start = index
        elif index - segment_start > min_duration * frame_rate:
            within_range_segments.append((segment_start, index))
            segment_start = None
    
    # Aggiungi il simbolo corrispondente all'output per ciascun segmento
    output += str(symbol * len(within_range_segments))

# Stampa l'output
print(output)

# Chiudi il file WAV
wav.close()
