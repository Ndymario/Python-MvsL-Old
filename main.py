########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

# Enable/Disable DEBUG mode
DEBUG = True

# Enable/Disable Player 2
P2 = True

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
mario = Player(makeSprite("Sprites/Mario.png",15), -10)

if P2: #Experimental 
    luigi = Player(makeSprite("Sprites/Luigi.png",15), -15, 0.2, 1, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d,50)
    players = mario, luigi
else:
    players = [mario]
    
# Load the Player's sprites
for player in players:
    showSprite(player.playerSprite)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    # Get player inputs
    for player in players:
        # Turn inputs into movement
        player.RefineInput(keys, level, player.playerSprite, frame)        

        # Debug
        if (DEBUG):
            print(player)
    
        # Calculate and update position
        player.calculatePosition()
        updated_position = player.check_collision(level)        

        # Check for death
        player.death()

        
        
    # Limit the framerate to 60 FPS
    tick(60)

    #Render the screen
    screen.fill(WHITE)
    for tile in level.tiles:
        for w in range(int(tile.width / 16)):
            for h in range(int(tile.height / 16)):
                screen.blit(pygame.image.load(tile.tile_image), [tile.x + (w * 16), tile.y - (h * 16)])

    # Update the player's sprite location
    for player in players:
        moveSprite(player.playerSprite, player.x, player.y + player.height)

    updateDisplay()
    # Limits the frame rate of sprites (60 FPS walk cycle is bad)
    if clock() > nextFrame:
        frame = (frame+1)%3
        nextFrame += 60
