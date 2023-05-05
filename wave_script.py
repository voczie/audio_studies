import wave

def print_parameters(wav_file):
    print("Number of Channels: ", wav_file.getnchannels())
    print("Sample Width: ", wav_file.getsampwidth())
    print("Frame Rate: ", wav_file.getframerate())
    print("Number of Frames: ", wav_file.getnframes())
    print("Parameters: ", wav_file.getparams())
    print("Audio Time: ", audio_time(wav_file))
    print('\n')

def audio_time(wav_file):
    return wav_file.getnframes() / wav_file.getframerate()

def get_frames(wav_file):
    frames = wav_file.readframes(-1) # read all frames, returns a object bytes of int
    return frames # frames length will be twice the number o frames size, cause the sample width is 2

def create_audio(filename, n_channels, sample_width, framerate, frames):
    new_audio = wave.open(f"{filename}.wav", "wb")

    new_audio.setnchannels(n_channels)
    new_audio.setsampwidth(sample_width)
    new_audio.setframerate(framerate)
    new_audio.writeframes(frames)

    new_audio.close()

if __name__ == "__main__":
    korg_c2 = wave.open("resources/korg_c2.wav", "rb")
    korg_c3 = wave.open("resources/korg_c3.wav", "rb")
    korg_c4 = wave.open("resources/korg_c4.wav", "rb")
    yamaha_c2 = wave.open("resources/yamaha_c2.wav", "rb")

    print("Korg Bass - C2")
    print_parameters(korg_c2)
    korg_c2.close()
    print('\n')

    print("Korg Bass - C3")
    print_parameters(korg_c3)
    korg_c3.close()
    print('\n')

    print("Korg Bass - C4")
    print_parameters(korg_c4)
    korg_c4.close()
    print('\n')

    print("Yamaha Bass - C2")
    print_parameters(yamaha_c2)
    yamaha_frames = get_frames(yamaha_c2)
    yamaha_c2.close()
    print('\n')

    create_audio("resources/new_audio", 1, 2, 44100, yamaha_frames)