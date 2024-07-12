# Local Imports
import pygame
import os
import random 
import sys


global random_song



def play_theme(folder: str, fade_in_duration: int = 1000, track: str = None):
    '''
    Function to play a theme from a folder
    '''

    global random_song
    random_song = random.choice(os.listdir(folder))
    
    full_path = os.path.join(folder, random_song)
    print (folder)
    if r'Background Noises' in folder:
        # stop any currently playing music
        channel1.stop()
        channel1.play(pygame.mixer.Sound(full_path), fade_ms=fade_in_duration, loops=-1)
    else:
        
        channel2.play(pygame.mixer.Sound(full_path), fade_ms=fade_in_duration, loops=-1)

    

    


def stop_music(fade_out_duration: int = 4000):
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
    pygame.mixer.set_num_channels(2)

    # create separate Channel objects for simultaneous playback
    global channel1, channel2
    channel1 = pygame.mixer.Channel(0) # argument must be int
    channel2 = pygame.mixer.Channel(1)

    # Get the project root directory
    repo_root = os.path.abspath(os.path.dirname(__file__))

    # Location of music theme folders
    adventure_folder = os.path.join(repo_root, r'Adventure')
    combat_folder = os.path.join(repo_root, r'Combat')
    background_folder = os.path.join(repo_root, r'Background Noises')

    current_theme = None # Variable to store the current theme


    running = True

    while running:

       

        # Print Menu of Options
        print(f'Select a musically theme for your DnD game! \n1. Adventure \n2. Combat \n3. Background Noiises \n4. Volume Up \n5. Volume down\n6. Exit\n\n')

        
        selection = int(input('Enter the number of your selection: '))
            # Check Selection
        if selection == 1:

            # Check for currently playing music
            if current_theme:
               stop_music()

            # Play Adventure Theme
            play_theme(adventure_folder)
            
            # Set the current theme1
            current_theme = 'Adventure'
            # Console Log
            print(f'Adventure Theme Selected - {random_song}' )
            
            

            
        elif selection == 2:
        
            # Check for currently playing music
            if current_theme:
                stop_music()
            
            # Play Adventure Theme
            play_theme(combat_folder)
            # Set the current theme
            current_theme = 'Combat'
            # Console Log
            print(f'Combat Theme Selected - {random_song}')
        
        elif selection == 3:

            # Background Menu
            print(f'Select a background noise for your DnD game! \n1. Cave \n2. Forest \n3. Tavern \n4. Town \n5. Rain \n6. Exit\n\n')
            bg_selection = int(input('Enter the number of your selection: '))
            # Play Background Noises
            #play_background(background_folder, background_selection)
            
            

            match bg_selection:
                case 1:
                    # Get file path for subfolder selected
                    folder = os.path.join(background_folder, r'Cave')
                    play_theme(folder)
                case 2:
                    # Get file path for subfolder selected
                    folder = os.path.join(background_folder, r'Forest')
                    play_theme(folder)
                case 3:
                    # Get file path for subfolder selected
                    folder = os.path.join(background_folder, r'Tavern')
                    play_theme(folder)
                case 4:
                    # Get file path for subfolder selected
                    folder = os.path.join(background_folder, r'Town')
                    play_theme(folder)
                case 5:
                    # Get file path for subfolder selected
                    folder = os.path.join(background_folder, r'Rain')
                    play_theme(folder)
                case 6:
                    channel1.stop()
                    
                case _:
                    print('Invalid Selection')
                    sys.exit()
                    

            


        elif selection == 4:
            # Volume Up
            channel2.set_volume(channel2.get_volume() + 0.1)
            print(f'Volume Up: {channel2.get_volume()}')

        elif selection == 5:
            # Volume Down
            channel2.set_volume(channel2.get_volume() - 0.1)
            print(f'Volume Down: {channel2.get_volume()}')     

        elif selection == 6:
            running = False
            print('Exiting...')

# Init Main Script
__init__ = ["main"]
main()


 # Volume control
 