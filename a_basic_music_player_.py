# -*- coding: utf-8 -*-
"""a basic music player .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fE6aWF3yO4Gv_fDP8FYmkBuH6KJT1-74
"""

import pygame
import time

# Initialize the mixer module in pygame
pygame.mixer.init()

# Function to load a music file
def load_music(file_path):
    try:
        pygame.mixer.music.load(file_path)
        print(f"Loaded: {file_path}")
    except pygame.error as e:
        print(f"Error loading {file_path}: {e}")

# Function to play the loaded music
def play_music():
    if pygame.mixer.music.get_busy():
        print("Music is already playing!")
    else:
        pygame.mixer.music.play()
        print("Playing music...")

# Function to pause the music
def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        print("Music paused.")
    else:
        print("No music is playing to pause.")

# Function to resume the music
def resume_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()
        print("Music resumed.")
    else:
        print("Music is already playing or has not been paused.")

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

if __name__ == "__main__":
    # Example music file path
    music_file = "your_music_file.mp3"  # Replace with your own music file path

    # Load the music file
    load_music(music_file)

    # Control the music player
    while True:
        print("\nCommands: play, pause, resume, stop, quit")
        command = input("Enter command: ").lower()

        if command == "play":
            play_music()
        elif command == "pause":
            pause_music()
        elif command == "resume":
            resume_music()
        elif command == "stop":
            stop_music()
        elif command == "quit":
            stop_music()
            break
        else:
            print("Unknown command. Please try again.")

        time.sleep(1)  # Small delay to allow music commands to take effect