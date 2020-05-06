########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
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

<<<<<<< HEAD
#---------------------------------#
##########--BEGIN CLASSES--##########
=======
levelchunk1 = []

level = Level("Levels/1-1.lvl")

for tile in level.tiles:
    levelchunk1.append(Tile("Tiles/Grass_Top.png", 1, tile["x"] * 16, tile["y"] * 16, tile["width"] * 16, tile["height"] * 16))

##########--BEGIN CLASSES--##########

# Class for the player
class Player(object):
    def __init__(self, skin = None, height = 0, weight = 0.2, player_number = 0):
        self.player_number = player_number
        # Used to determine what sprites to load for the player
        self.skin = skin
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

        elif((player.y_velocity >= 0.0) and (player.check_fall() ==False)):
            if p_weight <= gravity:
                p_weight += gravity
            else:
                p_weight = gravity

            player.y_velocity += (player.weight * p_weight)
            if player.y_velocity < VSPEED_CAP:
                player.y_velocity = VSPEED_CAP

        else:
            if player.check_fall() != False:
                player.y_velocity = 0.0
                player.y = player.check_fall()
    
    def death(self):
        pass

    def respawn(self):
        pass
    
    def check_jump(self):
        for tile in levelchunk1:
            if (player.y == tile.top) and player.x <= tile.width + tile.x and player.x >=tile.x - tile.x: 
                return True
        return False

    def check_fall(self):
        for tile in levelchunk1:
            if (player.y >= tile.top) and player.y <= tile.top + 10 and player.x <= tile.width + tile.x and player.x >=tile.x - 16: 
                return tile.top
        return False

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
>>>>>>> 99f3c28ba75db2e0a9c4a3722fb0839d4a7d15ae
  
##########--END CLASSES--##########
#---------------------------------#
##########--BEING FUNCTIONS--######
<<<<<<< HEAD
=======

def check_colision():
    for tile in levelchunk1:
        if (player.x >= tile.left -11) and player.x <= tile.right + 8 and player.y -1 > tile.top and player.y - 1 <=tile.y: 
            if player.x - tile.left-11 < tile.right - player.x + 3:
                return tile.left -11
            else:
                return tile.right + 8
    return False
>>>>>>> 99f3c28ba75db2e0a9c4a3722fb0839d4a7d15ae
  
##########--END FUNCTIONS--########
#---------------------------------#
##########-Begin Main Code-########

# Load Level Data
levelchunk1 = []
level = Level("Levels/1-1.lvl")

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
        if player.check_jump(level) == True:
            if (player.y_velocity > VSPEED_CAP):
                player.y_velocity = VSPEED_CAP
            elif (player.y_velocity < VSPEED_CAP):
                player.y_velocity = VSPEED_CAP
        else:
            # If the player can't jump, continue to apply gravity
            player.gravity(GRAVITY,level)

    # Apply gravity to the player
    else:
        player.gravity(GRAVITY,level)
    
    if (DEBUG):
        print(player)

    # Limit the framerate to 60 FPS
    clock.tick(60)

    player.calculatePosition()
    if level.hit_under_tile(player.x,player.y - 33,player) != False:
        player.y = level.hit_under_tile(player.x,player.y - 33,player).y + 33
        player.y_velocity = 0.0
    if player.check_fall(level) != False:
        player.y = player.check_fall(level)
        player.y_velocity = 0.0
    if player.check_colision(level) != False:
        player.x = player.check_colision(level)
        player.x_velocity = 0.0
    #Render the screen
    screen.fill(BLACK)
<<<<<<< HEAD
    for tile in level.tiles:
        for w in range(int(tile.width / 16)):
            for h in range(int(tile.height / 16)):
=======
    for tile in levelchunk1:
        for w in range(tile.width // 16):
            for h in range(tile.height // 16):
>>>>>>> 99f3c28ba75db2e0a9c4a3722fb0839d4a7d15ae
                screen.blit(pygame.image.load(tile.tile_image), [tile.x + (w * 16), tile.y + (h * 16)])
    screen.blit(pygame.image.load(player.skin), [player.x, player.y - player.height])
    pygame.display.flip()





