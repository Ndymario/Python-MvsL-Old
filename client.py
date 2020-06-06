########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

##########--Begin System Level Stuff--##########

# Import things I might need
from pygame_functions import *
import sys
from level import *
from player import *
from cmap import *

# Allows us to use another folder than the folder this file is located
sys.path.insert(1, "./Sprites")

##########--End System Level Stuff--##########


#---------------------------------#


##########--BEGIN CLASSES--##########
  
##########--END CLASSES--##########


#---------------------------------#


##########--BEGIN FUNCTIONS--######

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def game_intro():
    screen = screenSize(800, 600, None, None, False)

    intro = True

    while intro:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keys[pygame.K_SPACE]:
            intro = False
                
        screen.fill(WHITE)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Mario vs Luigi", largeText)
        TextRect.center = ((800/2),(600/2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        tick(15)
    
    # Run the game if the title screen is cleared
    gameLoop()

def gameLoop():

    # Setup the screen and other display stuff
    # Note: WIDTH & HEIGHT are imported from player.py!
    screen = screenSize(WIDTH, HEIGHT, None, None, False)

    inGame = True

    # Load Level Data
    levelchunk1 = []

    # This recreates the collision map automatically
    cmap = CMap("Cmap/1-1.cmap")
    cmap.create_cmap("Levels/1-1.lvl")
    level = Level("Levels/1-1.lvl")

    # Frame handler (used for any sprite animation)
    frame = 0
    superFrame = 0
    nextFrame = clock()

    # Create a player
    mario = Player("Sprites/Mario/")

    if P2: #Experimental 
        luigi = Player("Sprites/Luigi/", [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q, pygame.K_LSHIFT]\
                    , 1, 15, 100, 10, 20)
        players = [mario, luigi]
    else:
        players = [mario]
        
    # Load the Player's sprites
    for player in players:
        # The powerup handler already creates the player sprite, so use this to initalize the players
        player.powerupHandler(0)

    while inGame:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: sys.exit()
        keys = pygame.key.get_pressed()

        # Get player inputs
        for player in players:
            # Turn inputs into movement
            player.RefineInput(keys, cmap, player.playerSprite, player.last_held_direction, frame, superFrame, level)        
        
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
                # Make the Bros. Small
                if keys[pygame.K_0]:
                    mario.powerupHandler(0)
                    luigi.powerupHandler(0)

                # Make both Bros. Super
                if keys[pygame.K_1]:
                    mario.powerupHandler(1)
                    luigi.powerupHandler(1)
                
                # Make Mario Fire Mario
                if keys[pygame.K_2]:
                    mario.powerupHandler(2)

                # Return to the title screen
                if keys[pygame.K_9]:
                    # Remove all player sprites 
                    for player in players:
                        hideSprite(player.playerSprite)
                    # Remove all players from the player list
                    players.clear()

                    # Load the title screen
                    game_intro()
            
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
            superFrame = (superFrame+1)%3
            nextFrame += 60

##########--END FUNCTIONS--########


#---------------------------------#


##########-Begin Main Code-########

# Enable/Disable DEBUG mode
DEBUG = True

# Enable/Disable Player 2
P2 = True

# Define some constants
BLACK = (0, 0, 0)
WHITE  = (255, 255, 255)


# Initialize the game to the title screen

game_intro()

###########-End Main Code-#########