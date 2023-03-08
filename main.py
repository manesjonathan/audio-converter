import os

from pydub import AudioSegment

# Define the directory containing the audio files
directory = "files/"

# Iterate through the folder and convert all .wma and .wav files to .mp3
for file in os.listdir(directory):
    if file.endswith(".wma"):
        wma_audio = AudioSegment.from_file(os.path.join(directory, file), format="asf")
        wma_audio.export(os.path.join(directory, file.replace(".wma", ".mp3")), format="mp3")
        print("Converted " + file + " to mp3")
    elif file.endswith(".wav"):
        wav_audio = AudioSegment.from_file(os.path.join(directory, file), format="wav")
        wav_audio.export(os.path.join(directory, file.replace(".wav", ".mp3")), format="mp3")
        print("Converted " + file + " to mp3")
    # if the file is already a .mp3, ignore it
    elif file.endswith(".mp3"):
        continue
