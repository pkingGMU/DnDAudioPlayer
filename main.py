# Local Imports

def theme_selector(selection: int):
    '''
    Input: selection (int)
    '''

    # Check Selection
    if selection == 1:
        print('Adventure Theme Selected')
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