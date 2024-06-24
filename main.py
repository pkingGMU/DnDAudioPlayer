# Local Imports
from pydub import AudioSegment
from pydub.playback import play
import time
import os
import random 


def get_random_song(folder: str):
    '''
    Function to get a random song from a folder
    '''
    return random.choice(os.listdir(folder))

def play_music(song: str):
    '''
    Function to play music
    '''
    audio = AudioSegment.from_file(song, format='mp3')

    print(f'Playing Music... {song}')


def theme_selector(selection: int):
    '''
    Input: selection (int)
    '''

    # Check Selection
    if selection == 1:
        # Console Log
        print('Adventure Theme Selected')
        # Play Random Adventure Theme from the Adventure Folder
        play_music(get_random_song(r'C:\Users\patk1\OneDrive\Desktop\Git Hub\DnDAudioPlayer\Adventure'))
    elif selection == 2:
        print('Combat Theme Selected')


def main():
    '''
    Main function to run the script
    '''

    # Print Menu of Options
    print(f'Select a musically theme for your DnD game! \n1. Adventure \n2. Combat')
    theme_selector(int(input('Selection: ')))

# Init Main Script
__init__ = ["main"]
main()