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

# This recreates the collision map automatically
cmap = CMap("Cmap/1-1.cmap")
cmap.create_cmap("Levels/1-1.lvl")
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
mario = Player("Sprites/Mario/")

if P2: #Experimental 
    luigi = Player("Sprites/Luigi/", [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]\
                   , 1, 25, 100, 16, 20)
    players = [mario, luigi]
else:
    players = [mario]
    
# Load the Player's sprites
for player in players:
    spriteSheet = player.powerupHandler(player.powerupState)
    player.playerSprite = makeSprite(spriteSheet, 18)
    showSprite(player.playerSprite)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()
    keys = pygame.key.get_pressed()

    # Get player inputs
    for player in players:
        # Turn inputs into movement
        player.RefineInput(keys, cmap, player.playerSprite, player.last_held_direction, frame, level)        
    
        # Calculate and update position
        player.calculatePosition()
        updated_position = player.check_collision(cmap)        
        player.x = updated_position[0]
        player.y = updated_position[1]
        player.x_velocity = updated_position[2]
        player.y_velocity = updated_position[3]

        # Check for death
        player.death()

    # Debug
        if (DEBUG):
            if keys[pygame.K_0]:
                mario.hurt()

            if keys[pygame.K_1]:
                mario.powerupState = 2
                mario.hurt()
        
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
        moveSprite(player.playerSprite, player.x + player.draw_width, player.y + player.draw_height)

    updateDisplay()
    # Limits the frame rate of sprites (60 FPS walk cycle is bad)
    if clock() > nextFrame:
        frame = (frame+1)%2
        nextFrame += 60
