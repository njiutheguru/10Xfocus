import pygame
from pyinstaller_file import Resource
import os
import sys


# for pyinstaller to locate assets and data
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Initialize the pygame mixer
class Sound:
    def __init__(self):

        pygame.mixer.init()
        # Load a sound file
        sound_file = resource_path("ring1.mp3")
        sound = pygame.mixer.Sound(sound_file)
        # sound.set_volume(0.9)
        # Play the sound
        sound.play()
        # Wait for the sound to finish playing Below line must be applied
        pygame.time.wait(int(sound.get_length() * 1000))
