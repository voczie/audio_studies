import pyaudio
from wave_script import create_audio

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt32
N_CHANNELS = 1
SAMPLE_RATE = 44100

aud = pyaudio.PyAudio()

stream = aud.open(
    format = FORMAT,
    channels = N_CHANNELS,
    rate = SAMPLE_RATE,
    input = True,
    frames_per_buffer = FRAMES_PER_BUFFER
)

print("Start recording...")

seconds = 5
frames = []

for i in range(0, int((SAMPLE_RATE / FRAMES_PER_BUFFER) * seconds)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
aud.terminate()

print("Stop recording")


# saving recorded audio
sample_width = aud.get_sample_size(FORMAT)
frames_audio = (b"".join(frames))

create_audio(
    filename ="resources/mic_record", 
    n_channels = N_CHANNELS, 
    sample_width = sample_width,
    framerate = SAMPLE_RATE,
    frames = frames_audio
)