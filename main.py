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
def Friction():
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

def HorizontalVelocity(last_held_direction, skidding):
    if (last_held_direction == "right"):
            # Cap the player's horizontal speed to the right
            if (player.x_velocity <= SPEED_CAP):
                if (player.x_velocity < 0):
                    if (skidding == False):
                        # Update the player to their skidding animation when turning around
                        changeSpriteImage(playerSprite, 4*3)
                        skidding = True
                    else:
                        skidding = False
                player.x_velocity += ACCELERATION
                if player.x_velocity >= SPEED_CAP:
                    player.x_velocity = SPEED_CAP
            elif (player.x_velocity >= SPEED_CAP):
                player.x_velocity = SPEED_CAP
    
    elif (last_held_direction == "left"):
            # Cap the player's horizontal speed to the left
            if (player.x_velocity >= -SPEED_CAP):
                if (player.x_velocity > 0):
                    if (skidding == False):
                        # Update the player to their skidding animation when turning around
                        changeSpriteImage(playerSprite, 4*3+1)
                        skidding = True
                else:
                    skidding = False
                player.x_velocity -= ACCELERATION
                if player.x_velocity <= -SPEED_CAP:
                    player.x_velocity = -SPEED_CAP
            elif (player.x_velocity <= -SPEED_CAP):
                player.x_velocity = -SPEED_CAP

def VerticalVelocity():
    if (player.y_velocity > VSPEED_CAP):
        player.y_velocity = VSPEED_CAP
    elif (player.y_velocity < VSPEED_CAP):
        player.y_velocity = VSPEED_CAP

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
screen = screenSize(WIDTH, HEIGHT)

# Define some in game constants (used for the Physics "engine")
SPEED_CAP = 8.0
VSPEED_CAP = -8.0
FRICTION = .2
ACCELERATION = 0.1
V_ACCELERATION = 0.1
GRAVITY = 2.5

# Frame handler (used for any sprite animation)
frame = 0
nextFrame = clock()

# Create a player
player = Player("Sprites/Mario.png", -10)
playerSprite = makeSprite(player.skin, 15)

# Define player controls
up = pygame.K_UP
down = pygame.K_DOWN
left = pygame.K_LEFT
right = pygame.K_RIGHT
print(player.y)

# Display Sprites as they're needed
showSprite(playerSprite)

# Define misc. Player variables
last_held_direction = "right"
idle = False
skidding = False

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    # Update the player's sprite when idling
    if (player.check_jump(level) == True):
        if (idle == False):
            # If the last input was to the right, face the Player's sprite to the right
            if (last_held_direction == "right"):
                changeSpriteImage(playerSprite, 3*3+1)
                updated = True
            # Otherwise, face Mario's sprite to the left
            else:
                changeSpriteImage(playerSprite, 0*3+1)
                updated = True

    # Set the last held direction to right, and update the player's walk animation if they're on the ground
    if keys[right]:
        last_held_direction = "right"

        # Check to see if the player is on the ground before applying the sprite change
        if (player.check_jump(level) == True):
            # Update the player's sprite when walking
            changeSpriteImage(playerSprite, 3*3+frame)

        HorizontalVelocity(last_held_direction, skidding)
 
    # Set the last held direction to left, and update the player's walk animation if they're on the ground           
    elif keys[left]:
        last_held_direction = "left"

        # Check to see if the player is on the ground before applying the sprite change
        if (player.check_jump(level) == True):
            # Update the player's sprite when walking
            changeSpriteImage(playerSprite, 0*3+frame)

        HorizontalVelocity(last_held_direction, skidding)
    
    elif keys[down]:
        # If the player is on the ground, make them duck
        if player.check_jump(level) == True:
            changeSpriteImage(playerSprite, 5*3 - 1)
        # Apply friction to the player
        Friction()
            
    # Apply friction to the player if they are not holding a button or ducking
    # (slow them to a hault)
    else:
        # Apply friction to the player
        Friction()

    # Generate player y velocity
    # Check to see if the player can jump
    if keys[up]:
        if player.check_jump(level) == True:
            # If the last input was to the right, face the Player's sprite to the right
            if (last_held_direction == "right"):
                changeSpriteImage(playerSprite, 2*3+frame)
            # Otherwise, face Mario's sprite to the left
            else:
                changeSpriteImage(playerSprite, 1*3+frame)
            VerticalVelocity()

        else:
            # If the last input was to the right, face Mario's sprite to the right
            if (last_held_direction == "right"):
                changeSpriteImage(playerSprite, 2*3+frame)
            # Otherwise, face Mario's sprite to the left
            else:
                changeSpriteImage(playerSprite, 1*3+frame)
            # If the player can't jump, continue to apply gravity
            player.gravity(GRAVITY,level)

    # Apply gravity to the player
    elif (player.check_jump(level) == False):
        # If the last input was to the right, face Mario's sprite to the right
        if (last_held_direction == "right"):
            changeSpriteImage(playerSprite, 2*3+frame)
        # Otherwise, face Mario's sprite to the left
        else:
            changeSpriteImage(playerSprite, 1*3+frame)
        player.gravity(GRAVITY,level)

    else:
        player.gravity(GRAVITY,level)
    
    if (DEBUG):
        print(player)

    # Limit the framerate to 60 FPS
    tick(60)

    player.calculatePosition()
    updated_position = player.check_collision(level)

    
    #Render the screen
    screen.fill(WHITE)
    for tile in level.tiles:
        for w in range(int(tile.width / 16)):
            for h in range(int(tile.height / 16)):
                screen.blit(pygame.image.load(tile.tile_image), [tile.x + (w * 16), tile.y - (h * 16)])

    # Update the player's sprite location
    moveSprite(playerSprite, player.x, player.y + player.height)

    # Limits the frame rate of sprites (60 FPS walk cycle is bad)
    if clock() > nextFrame:
        frame = (frame+1)%3
        nextFrame += 60
