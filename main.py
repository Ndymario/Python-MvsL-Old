########################################################################
#   Author: Nolan Y.                                                   #
#                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

# Import things I might need
import pygame
import sys
from pygame.locals import *

# Allows us to use another folder than the folder this file is located
sys.path.insert(1, "./Sprites")

##########--BEGIN CLASSES--##########

# Class for the player
class Player(object):
    def __init__(self, player_skin = None, player_number = 0):
        self.player_number = player_number
        self.player_skin = player_skin
        self.x = 100
        self.y = 100
        self.x_velocity = 0
        self.y_velocity = 0

##########--END CLASSES--##########

# Inialize pygame stuff
pygame.init()

# Make the window title
pygame.display.set_caption("Mario vs Luigi")

# Create a player
player = Player("Sprites/idle.png")

# Define some constants
SIZE = WIDTH, HEIGHT = 320, 240
BLACK = (0, 0, 0)

# Setup the screen and display stuff
screen = pygame.display.set_mode(SIZE)
skin = pygame.image.load(player.player_skin)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    #Render the screen
    screen.fill(BLACK)
    screen.blit(skin, [player.x, player.y])
    pygame.display.flip()
