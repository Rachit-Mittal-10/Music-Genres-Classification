#* Neccessary Imports
import numpy as np
import os
import random
from glob import glob
import librosa
import pandas as pd
import gc
gc.enable()

#* This will make the list of all the audio path in the directory 'genres_original'
def openAudioFiles():
    audio_files = glob("genres_original/*/*.wav")
    if audio_files:
        return audio_files
    else:
        return "No files matched the path"


def openAudioFilesRandom(n):
    audio_files = list()
    subdirectories = os.listdir("./genres_original")
    for subdirectory in subdirectories:
        subdirectoryPath = os.path.join("./genres_original",subdirectory)
        if os.path.isdir(subdirectoryPath):
            files = os.listdir(subdirectoryPath)
            selected_files = random.sample(files,n)
            full_path_selected_files = [os.path.join(subdirectoryPath,wav_file) for wav_file in selected_files]
            audio_files.extend(full_path_selected_files)
    return audio_files

#* This function will augment the audio
def augment_audio(y, sr):
    # Pitch shifting
    y_pitch_shifted = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=4)
    # Time stretching
    y_time_stretched = librosa.effects.time_stretch(y=y, rate=1.5)
    # Adding noise
    noise = np.random.randn(len(y))
    y_noisy = y + 0.005 * noise
    return (y_pitch_shifted, y_time_stretched, y_noisy)

def trimAudio(y):
    y_trimmed, _ = librosa.effects.trim(y, top_db=30)
    return y_trimmed

#* This function will extract features such as stft,spectrogram, mfcc for each audio file
def extract2DFeatures(audio_path):
    y,sr = librosa.load(audio_path)
    # augment_audios = augment_audio(y,sr)
    stft = np.abs(librosa.stft(y))
    spectrogram = librosa.feature.melspectrogram(y=y,sr=sr,n_mels=128)
    mfcc = librosa.feature.mfcc(S=spectrogram)
    gc.collect()
    return (stft,spectrogram,mfcc)

def main():
    audio_files = openAudioFiles()
    # audio_files = openAudioFilesRandom(2)
    if not type(audio_files) == list:
        pass
    # mfccs = list()
    # melspectrograms = list()
    # stfts = list()
    for i, audio_file in enumerate(audio_files[500:600]):
        features = extract2DFeatures(audio_path=audio_file)
        # mfccs.append(features[2])
        # melspectrograms.append(features[1])
        # stfts.append(features[0])
        print(f"{i} | {features[0].shape} | {features[1].shape} | {features[2].shape}")
    

main()