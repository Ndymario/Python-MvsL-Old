########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

# Enable/Disable DEBUG mode
DEBUG = True

# Enable/Disable Player 2
P2 = False

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

if P2:
    player2 = Player("Sprites/Luigi.png", -15, 0.2, 1, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

playerSprite = makeSprite(player.skin, 15)

if P2:
    player2Sprite = makeSprite(player2.skin, 15)

# Display Sprites as they're needed
if P2:
    showSprite(player2Sprite)
showSprite(playerSprite)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    # Get player inputs
    player.RefineInput(keys, level, playerSprite, frame)
    if P2:
        player2.RefineInput(keys, level, player2Sprite, frame)
    
    if (DEBUG):
        print(player)

    # Limit the framerate to 60 FPS
    tick(60)

    player.calculatePosition()
    if P2:
        player2.calculatePosition()

    updated_position = player.check_collision(level)
    if P2:
        updated_position = player2.check_collision(level)

    #Render the screen
    screen.fill(WHITE)
    for tile in level.tiles:
        for w in range(int(tile.width / 16)):
            for h in range(int(tile.height / 16)):
                screen.blit(pygame.image.load(tile.tile_image), [tile.x + (w * 16), tile.y - (h * 16)])

    # Update the player's sprite location
    moveSprite(playerSprite, player.x, player.y + player.height)
    if P2:
        moveSprite(player2Sprite, player2.x, player2.y + player2.height)
    updateDisplay()
    # Limits the frame rate of sprites (60 FPS walk cycle is bad)
    if clock() > nextFrame:
        frame = (frame+1)%3
        nextFrame += 60
