import wave
import matplotlib.pyplot as plt
import numpy as np
from wave_script import audio_time

def plot(audio_time, times, signal):
    plt.figure(figsize=(15, 5))
    plt.plot(times, signal_array)
    plt.title("Audio Signal")
    plt.ylabel("Signal Wave")
    plt.xlabel("Time (in seconds)")
    plt.xlim(0, audio_time)
    plt.show()

bass = wave.open("resources/korg_c3.wav", "rb")

# Important parameters
sample_rate = bass.getframerate()
num_samples = bass.getnframes()
signal_wave = bass.readframes(-1) # get all frames
audio_time = audio_time(bass)

bass.close()

# as "signal_wave" is a 'bytes' object, we will create a numpy array from it
signal_array = np.frombuffer(signal_wave, dtype=np.int32)

# creates an evenly spaced numbers from the number of samples, starting at 0, ending at audio_time
times = np.linspace(0, audio_time, num=num_samples)

plot(audio_time, times, signal_array)