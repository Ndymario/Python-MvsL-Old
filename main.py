########################################################################
#   Author: Nolan Y.                                                   #
#                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

# Enable/Disable DEBUG mode
DEBUG = True

# Import things I might need
import pygame
import sys
from level import *

# Allows us to use another folder than the folder this file is located
sys.path.insert(1, "./Sprites")

##########--BEGIN CLASSES--##########

# Class for the player
class Player(object):
    def __init__(self, player_skin = None, height = 0, weight = 0.2, player_number = 0):
        self.player_number = player_number
        # Used to determine what sprites to load for the player
        self.player_skin = player_skin
        self.x = 100
        self.y = 100
        self.x_velocity = 0.00
        self.y_velocity = 0.00
        # Number is from height of the player sprite in pixles
        self.height = height
        self.weight = weight
    
    def gravity(self, gravity):
        p_weight = self.weight
        if ((player.y_velocity >= VSPEED_CAP) and (player.y_velocity < 0)):
            if p_weight <= gravity:
                    p_weight += gravity
            else:
                p_weight = gravity
            player.y_velocity += (player.weight * p_weight)

            if player.y_velocity >= 0:
                player.y_velocity = 0.0

        elif((player.y_velocity >= 0.0) and (player.y < tile.top)):
            if p_weight <= gravity:
                p_weight += gravity
            else:
                p_weight = gravity

            player.y_velocity += (player.weight * p_weight)
            if player.y_velocity < VSPEED_CAP:
                player.y_velocity = VSPEED_CAP

        elif player.y > tile.top:
            player.y_velocity = 0.0
    
    def death():
        pass

    def respawn():
        pass

    def calculatePosition(self):
        # Make it so the player wraps around on the left and right (if enabled)
        if (wrap_around):
            if (((player.x >= WIDTH - 10) and (player.x <= WIDTH)) and player.x_velocity >= 0):
                player.x = 11
            elif ((player.x >= 0) and (player.x <= 10)) and (player.x_velocity <= 0):
                player.x = WIDTH - 11
        
        # Calculate the players next position using their coordinates
        # (This will probably be improved in the future)
        self.x += self.x_velocity
        self.y += self.y_velocity

    # Print stats of the player when called
    def __str__(self):
        return "Player X Velocity: {}\nPlayer Y Velocity: {}\nPlayer X: {}\nPlayer Y: {}"\
            .format(player.x_velocity, player.y_velocity, player.x, player.y)


##########--END CLASSES--##########
#---------------------------------#
##########--BEING FUNCTIONS--######


##########--END FUNCTIONS--#########

# Inialize pygame stuff
pygame.init()

clock = pygame.time.Clock()

# Make the window title
pygame.display.set_caption("Mario vs Luigi")

# Create a player
player = Player("Sprites/idle.png", 20)

# Define some constants
SIZE = WIDTH, HEIGHT = 320, 240
BLACK = (0, 0, 0)

# Setup the screen and other display stuff
screen = pygame.display.set_mode(SIZE)
skin = pygame.image.load(player.player_skin)

# Define some settings variables
wrap_around = True

# Define some in game constants (used for the Physics "engine")
SPEED_CAP = 8.0
VSPEED_CAP = -8.0
FRICTION = 0.1
ACCELERATION = 0.1
V_ACCELERATION = 0.1
GRAVITY = 2.5

# Define misc variables

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    # Generate player x velocity
    if keys[pygame.K_RIGHT]:
        # Cap the player's horizontal speed to the right
        if (player.x_velocity <= SPEED_CAP):
            player.x_velocity += ACCELERATION
            if player.x_velocity >= SPEED_CAP:
                player.x_velocity = SPEED_CAP
        elif (player.x_velocity >= SPEED_CAP):
            player.x_velocity = SPEED_CAP
            
    elif keys[pygame.K_LEFT]:
        # Cap the player's horizontal speed to the left
        if (player.x_velocity >= -SPEED_CAP):
            player.x_velocity -= ACCELERATION
            if player.x_velocity <= -SPEED_CAP:
                player.x_velocity = -SPEED_CAP
        elif (player.x_velocity <= -SPEED_CAP):
            player.x_velocity = -SPEED_CAP
    
    # Apply friction to the player if they are not holding a button (slow them to a hault)
    else:
        if ((player.x_velocity <= SPEED_CAP) and (player.x_velocity > 0)):
            if ((player.x_velocity <= SPEED_CAP) and (player.x_velocity > 0)):
                player.x_velocity -= FRICTION
                if player.x_velocity < 0:
                    player.x_velocity = 0.0
            else:
                player.x_velocity = 0.0

        elif ((player.x_velocity >= -SPEED_CAP) and (player.x_velocity < 0)):
            if ((player.x_velocity >= -SPEED_CAP) and (player.x_velocity < 0)):
                player.x_velocity += FRICTION
                if player.x_velocity > 0:
                    player.x_velocity = 0.0
            else:
                player.x_velocity = 0.0

    # Generate player y velocity
    # Check to see if the player can jump
    if keys[pygame.K_UP]:
        if (player.y >= tile.top):
            # Cap the player's vertical speed
            if (player.y_velocity > VSPEED_CAP):
                player.y_velocity = VSPEED_CAP
            elif (player.y_velocity < VSPEED_CAP):
                player.y_velocity = VSPEED_CAP
        else:
            # If the player can't jump, continue to apply gravity
            player.gravity(GRAVITY)

    # Apply gravity to the player
    else:
        player.gravity(GRAVITY)

    if (DEBUG):
        print(player)

    # Limit the framerate to 60 FPS
    clock.tick(60)

    player.calculatePosition()
    
    #Render the screen
    screen.fill(BLACK)
    screen.blit(pygame.image.load(tile.tile_image), [tile.x, tile.y])
    screen.blit(skin, [player.x, player.y - player.height])
    pygame.display.flip()