########################################################################
#   Author: Nolan Y.                                                   #
#                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

# Enable/Disable DEBUG mode
DEBUG = False

# Import things I might need
import pygame
import sys
from level import *
from player import *

# Allows us to use another folder than the folder this file is located
sys.path.insert(1, "./Sprites")

#---------------------------------#
##########--BEGIN CLASSES--##########
  
##########--END CLASSES--##########
#---------------------------------#
##########--BEING FUNCTIONS--######

def check_colision():
    for i in range(len(levelchunk1)):
        if (player.x >= levelchunk1[i-1].left -11) and player.x <= levelchunk1[i-1].right + 9 and player.y -1 > levelchunk1[i-1].top and player.y - 1 <=levelchunk1[i-1].y: 
            if player.x - levelchunk1[i-1].left-11 < levelchunk1[i-1].right - player.x:
                return levelchunk1[i-1].left -11
            else:
                return levelchunk1[i-1].right + 9
    return False
  
##########--END FUNCTIONS--########
#---------------------------------#
##########-Begin Main Code-########

# Inialize pygame stuff
pygame.init()

clock = pygame.time.Clock()

# Make the window title
pygame.display.set_caption("Mario vs Luigi")

# Define some constants
BLACK = (0, 0, 0)

# Setup the screen and other display stuff
screen = pygame.display.set_mode(SIZE)

# Define some in game constants (used for the Physics "engine")
SPEED_CAP = 8.0
VSPEED_CAP = -8.0
FRICTION = 0.1
ACCELERATION = 0.1
V_ACCELERATION = 0.1
GRAVITY = 2.5

# Define misc variables
frame = 1

# Create a player
player = Player("Sprites/idle.png",18)
playerL = Player("Sprites/idle.png",20)
players = [player,playerL]

# Define player controls
up = pygame.K_UP
down = pygame.K_DOWN
left = pygame.K_LEFT
right = pygame.K_RIGHT

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    # Generate player x velocity
    if keys[right]:
        # Cap the player's horizontal speed to the right
        if (player.x_velocity <= SPEED_CAP):
            player.x_velocity += ACCELERATION
            if player.x_velocity >= SPEED_CAP:
                player.x_velocity = SPEED_CAP
        elif (player.x_velocity >= SPEED_CAP):
            player.x_velocity = SPEED_CAP
 
            
    elif keys[left]:
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
    if keys[up]:
        if player.check_jump() == True:
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
    if player.check_fall() != False:
        player.y = player.check_fall()
        player.y_velocity = 0.0
    if check_colision() != False:
        player.x = check_colision()
        player.x_velocity = 0.0
    
    #Render the screen
    screen.fill(BLACK)
    for i in range(len(levelchunk1)):
        screen.blit(pygame.image.load(levelchunk1[i-1].tile_image), [levelchunk1[i-1].x, levelchunk1[i-1].y])
    screen.blit(pygame.image.load(player.skin), [player.x, player.y - player.height])
    pygame.display.flip()





