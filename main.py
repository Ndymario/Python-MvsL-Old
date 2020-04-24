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

# Allows us to use another folder than the folder this file is located
sys.path.insert(1, "./Sprites")

##########--BEGIN CLASSES--##########

# Class for the player
class Player(object):
    def __init__(self, player_skin = None, player_number = 0):
        self.player_number = player_number
        self.player_skin = player_skin
        self.x = 100.0
        self.y = 100.0
        self.x_velocity = 0.0
        self.y_velocity = 0.0
    
    def death():
        pass

    def calculatePosition(self):
        # Make it so the player wraps around on the left and right (if enabled)
        if (wrap_around):
            if player.x == WIDTH - 1 and player.x_velocity <= 0:
                player.x = 0
            elif player.x == 0 and player.x_velocity >= 0:
                player.x = WIDTH - 1
        
        # Calculate the players next position using their coordinates
        # (This will probably be improved in the future)
        self.x += self.x_velocity
        self.y += self.y_velocity

    # Print stats of the player when called
    def __str__(self):
        return "Player X Velocity: {}\nPlayer Y Velocity: {}\nPlayer X: {}\nPlayer Y: {}"\
            .format(player.x_velocity, player.y_velocity, player.x, player.y)


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

# Setup the screen and other display stuff
screen = pygame.display.set_mode(SIZE)
skin = pygame.image.load(player.player_skin)

# Define some settings variables
wrap_around = True

# Define some in game constants (used for the Physics "engine")
SPEED_CAP = 10.0
FRICTION = 0.2

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    # Generate player velocity
    if keys[pygame.K_RIGHT]:
        # Cap the player's horizontal speed to the right
        if (player.x_velocity <= SPEED_CAP):
            player.x_velocity += 0.5
        elif (player.x_velocity >= SPEED_CAP):
            player.x_velocity = SPEED_CAP
            
    elif keys[pygame.K_LEFT]:
        # Cap the player's horizontal speed to the left
        if (player.x_velocity >= -SPEED_CAP):
            player.x_velocity -= 0.5
        elif (player.x_velocity <= -SPEED_CAP):
            player.x_velocity = -SPEED_CAP
    
    else:
        if (player.x_velocity <= SPEED_CAP):
            if ((player.x_velocity < 1) and (player.x_velocity > 0)):
                player.x_velocity -= FRICTION
            else:
                player.x_velocity = 0.0

        elif (player.x_velocity >= SPEED_CAP):
            if ((player.x_velocity > -1) and (player.x_velocity < 0)):
                player.x_velocity += FRICTION
            else:
                player.x_velocity = 0.0
    print(player)

    player.calculatePosition()
    #Render the screen
    screen.fill(BLACK)
    screen.blit(skin, [player.x, player.y])
    pygame.display.flip()