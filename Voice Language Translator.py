from gtts import gTTS
import csv
from io import BytesIO
import pygame
import time

error = "No translation in dataset"

def load_dataset(file_path):
    dataset = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row)
    return dataset

def get_japanese_translation(english_sentence, dataset):
    for pair in dataset:
        if pair[0] == english_sentence:
            return pair[1]
    return error

file_path = r"C:\Users\Kaker\OneDrive\Desktop\Kakeru\Project 4th Sem\Language_Translator\en to ja.csv"
dataset = load_dataset(file_path)

# Initialize pygame mixer
pygame.mixer.init()

# Set the voice (you can adjust the index based on your preference)
pygame.mixer.music.set_volume(1.0)
voices = pygame.mixer.music.get_busy()
pygame.mixer.music.load("output.mp3")  # Load a blank audio file

# Your text input (replace this with your desired text)
input_text = "hello."

input_sentence = input_text
japanese_translation = get_japanese_translation(input_sentence, dataset)

print(japanese_translation)

# Use gTTS to convert the translated text into speech
tts = gTTS(japanese_translation, lang='ja')

# Save the gTTS audio to a BytesIO buffer
buffer = BytesIO()
tts.write_to_fp(buffer)
buffer.seek(0)

# Play the gTTS audio using pygame
pygame.mixer.music.load(buffer)
pygame.mixer.music.play()

# Wait for the audio to finish playing
while pygame.mixer.music.get_busy():
    time.sleep(0.1)
