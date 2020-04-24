#######################################################################
#   Author: Nolan Y.                                                  #
#                                                                     #
#   Description: My goal is to recreate the New Super Mario Bros.     #
#                DS gamemode Mario vs Luigi. Even if it's not perfect,#
#                it'll be a fun challenge!                            #
#######################################################################

# Import things I might need
import pygame
pygame.init()

# Define some constants
SIZE = WIDTH, HEIGHT = 320, 240
BLACK = 0, 0, 0

# Setup the screen
screen = pygame.display.set_mode(SIZE)

# Make some classes

# Class for the player
def Player(object):
    def __init__(self, player_skin, player_number = 0):
        self.player_number = player_number
        self.player_skin = player_skin
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        player_skin = ("idle.png")


##########--END CLASSES--##########

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    #Render the screen
    screen.fill(BLACK)
    screen.blit(player)
    pygame.display.flip()
