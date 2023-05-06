from pydub import AudioSegment

audio = AudioSegment.from_wav("resources/korg_c2.wav")

# increase the volume by 6dB
audio = audio + 6

# doubles the audio (2 times executed)
audio = audio * 2 

audio = audio.fade_in(200)

audio.export("resources/messed_c2.mp3", format = "mp3")
print("Done")