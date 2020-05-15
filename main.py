########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

# Enable/Disable DEBUG mode
DEBUG = True

# Import things I might need
from pygame_functions import *
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
##########--END FUNCTIONS--########
#---------------------------------#
##########-Begin Main Code-########

# Load Level Data
levelchunk1 = []
level = Level("Levels/1-1.lvl")

# Make the window title
pygame.display.set_caption("Mario vs Luigi")

# Define some constants
BLACK = (0, 0, 0)
WHITE  = (255, 255, 255)

# Setup the screen and other display stuff
# Note: WIDTH & HEIGHT are imported from player.py!
screen = screenSize(WIDTH, HEIGHT, None, None, False)

# Frame handler (used for any sprite animation)
frame = 0
nextFrame = clock()

# Create a player
player = Player("Sprites/Mario.png", -10)
playerSprite = makeSprite(player.skin, 15)

# Display Sprites as they're needed
showSprite(playerSprite)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    
    
    if (DEBUG):
        print(player)

    # Limit the framerate to 60 FPS
    tick(60)

    player.calculatePosition()
    updated_position = player.check_collision(level)

    # Get player inputs
    player.RefineInput(keys, level, playerSprite, frame)

    #Render the screen
    screen.fill(WHITE)
    for tile in level.tiles:
        for w in range(int(tile.width / 16)):
            for h in range(int(tile.height / 16)):
                screen.blit(pygame.image.load(tile.tile_image), [tile.x + (w * 16), tile.y - (h * 16)])

    # Update the player's sprite location
    moveSprite(playerSprite, player.x, player.y + player.height)
    updateDisplay()
    # Limits the frame rate of sprites (60 FPS walk cycle is bad)
    if clock() > nextFrame:
        frame = (frame+1)%3
        nextFrame += 60
