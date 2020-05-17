########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

# Enable/Disable DEBUG mode
DEBUG = False

# Enable/Disable Player 2
P2 = True

# Import things I might need
from pygame_functions import *
import sys
from level import *
from player import *
from cmap import *

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
cmap = CMap("Cmap/1-1.cmap")

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
mario = Player(makeSprite("Sprites/Mario.png",15), -26)

if P2: #Experimental 
    luigi = Player(makeSprite("Sprites/Luigi.png",15), -31, 0.2, 1, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d,50)
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
        player.RefineInput(keys, cmap, player.playerSprite, frame,level)        

        # Debug
        if (DEBUG):
            print(player)
    
        # Calculate and update position
        player.calculatePosition()
        updated_position = player.check_collision(cmap)        
        player.x = updated_position[0]
        player.y = updated_position[1]
        player.x_velocity = updated_position[2]
        player.y_velocity = updated_position[3]
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
