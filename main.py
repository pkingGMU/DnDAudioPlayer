# Local Imports
import pygame
import time
import os
import random 
import threading
import sys



def play_theme(folder: str, fade_in_duration: int = 20000, track: str = None):
    '''
    Function to play a theme from a folder
    '''

    

    if track is None:
        full_path = os.path.join(folder, random.choice(os.listdir(folder)))

        pygame.mixer.music.load(full_path)
        pygame.mixer.music.play(-1, fade_ms=fade_in_duration)  # -1 means loop indefinitely

    


def stop_music(fade_out_duration: int = 2000):
    '''
    Function to stop music
    '''
    pygame.mixer.music.fadeout(fade_out_duration)



def main():
    '''
    Main function to run the script
    '''

    # Init Pygame and Pygame Mixer
    pygame.init()
    pygame.mixer.init()

    # Location of music theme folders
    adventure_folder = r'C:\Users\patk1\OneDrive\Desktop\Git Hub\DnDAudioPlayer\Adventure'
    combat_folder = r'C:\Users\patk1\OneDrive\Desktop\Git Hub\DnDAudioPlayer\Combat'

    current_theme = None # Variable to store the current theme


    running = True

    while running:
        # Print Menu of Options
        print(f'Select a musically theme for your DnD game! \n1. Adventure \n2. Combat \n3. Exit\n\n')
        
        selection = int(input('Enter the number of your selection: '))
            # Check Selection
        if selection == 1:

            # Check for currently playing music
            if current_theme:
               stop_music()


            
            # Play Adventure Theme
            play_theme(adventure_folder )
            
            # Set the current theme
            current_theme = 'Adventure'
            # Console Log
            print('Adventure Theme Selected')
            
            

            
        elif selection == 2:\
        
            # Check for currently playing music
            if current_theme:
                stop_music()
            
            # Play Adventure Theme
            play_theme(combat_folder)
            # Set the current theme
            current_theme = 'Combat'
            # Console Log
            print('Combat Theme Selected')
            

        elif selection == 3:
            running = False
            print('Exiting...')

# Init Main Script
__init__ = ["main"]
main()