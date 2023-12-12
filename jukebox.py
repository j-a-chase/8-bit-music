######################################################################################################################################################
# Name: James A. Chase
# File: jukebox.py
# Date: 11 December 2023
# Description:
#
# Class file for Jukebox class.
#
######################################################################################################################################################

# imports
import pygame

class Jukebox():
    def __init__(self):

        # initialize mixer
        pygame.mixer.init()

        # set sample rate and bit depth
        pygame.mixer.set_num_channels(8)
        pygame.mixer.set_reserved(0)

        # play the song
        self.play()

    def play(self):
        pygame.mixer.music.load("./rickroll/rickroll.wav")

        # Play the .wav file
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy(): pygame.time.delay(1000)

if __name__ == '__main__': assert False, 'This is a class file. Please import its contents into another file.'
