########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

##########--Begin System Level Stuff--##########

# Import things I might need
import os
from raylibpy import *
from level import *
from player import *
from cmap import *

# Get the program's directory (used for relative pathing)
dirname = os.path.dirname(__file__)

##########--End System Level Stuff--##########


#---------------------------------#


##########--BEGIN CLASSES--##########

class Game(object):
    def __init__(self):
        self.players = []

    def gameIntro(self):
        screen_width = 800
        screen_height = 450

        init_window(screen_width, screen_height, "MvsL Recoded - Title Screen")

        intro = True

        while intro:
            begin_drawing()
            clear_background(RAYWHITE)
            draw_text('Press "A" to start!', 200, 200, 20, LIGHTGRAY)
            end_drawing()

            if is_key_down(KEY_A):
                intro = False
            
            # Run the game if the title screen is cleared
            if intro == False:
                close_window()
                self.gameLoop()

    def gameLoop(self):

        # Setup the screen and other display stuff
        screen_width = 800
        screen_height = 450
        init_window(screen_width, screen_height, "MvsL Recoded - In Game")

        inGame = True

        # This creates the collision map and the camera collision map from the level file automatically
        #TODO: Fix relative path for 1-1.lvl file (to run, you'll need the entire file path)
        cmap = CMap(dirname + "Cmap/1-1.cmap")
        cmap.create_cmap(dirname + "/Levels/1-1.lvl")
        cmap.create_camera_map(dirname + "/Levels/1-1.lvl")
        level = Level(dirname + "/Levels/1-1.lvl")

        # Frame handler (used for any sprite animation)
        frame = 0
        superFrame = 0
        nextFrame = get_time()

        # Create a player
        mario = Player(dirname + "/Sprites/Mario/")

        if P2: #Experimental 
            luigi = Player(dirname + "/Sprites/Luigi/", [KEY_W, KEY_S, KEY_A, KEY_D, KEY_Q, KEY_LEFT_SHIFT]\
                        , 1, 10, 20)
            self.players = [mario, luigi]
        else:
            self.players = [mario]

        # Start up the camera
        camera = Camera2D()
        camera.offset = Vector2(0, 0)
        camera.target = Vector2(mario.position[0] + 20, mario.position[1] + 20)
        camera.rotation = 0.0
        camera.zoom = 5.0

        # Load the Player's sprites
        for player in self.players:
            # The powerup handler already creates the player sprite, so use this to initalize the players
            player.powerupHandler(0)

        while inGame:

            # Create bounding box for the player sprites
            for player in self.players:
                player.frame_rec = Rectangle(0.0, 0.0, player.playerSprite.width/10, player.playerSprite.height)

            # Get player inputs
            for player in self.players:
                # Turn inputs into movement
                player.RefineInput(cmap, player.playerSprite, player.last_held_direction, frame, superFrame, level)        
            
                # Calculate and update player position
                player.calculatePosition(cmap)
                updated_position = player.check_collision(cmap)
                player.position = (updated_position[0], updated_position[1])
                player.velocity = (updated_position[2], updated_position[3])

                # Check for death
                player.death()

            # Debug
                if (DEBUG):
                    # Make the Bros. Small
                    if is_key_down(KEY_ZERO):
                        mario.powerupHandler(0)
                        luigi.powerupHandler(0)

                    # Make both Bros. Super
                    if is_key_down(KEY_ONE):
                        mario.powerupHandler(1)
                        luigi.powerupHandler(1)
                    
                    # Make Mario Fire Mario
                    if is_key_down(KEY_TWO):
                        mario.powerupHandler(2)

                    # Return to the title screen
                    if is_key_down(KEY_NINE):
                        self.clearGame()

            #Update the camera
            camera.position = Vector2(mario.position[0], mario.position[1])

            # Limit the framerate to 60 FPS
            set_target_fps(60)

            #Render the screen
            begin_drawing()

            clear_background(RAYWHITE)

            for tile in level.tiles:
                for w in range(int((tile.width) / 16)):
                    for h in range(int(tile.height / 16)):
                        # (Image to load, [(left coord of tile * width) - View, (bottom coord of tile - height)])
                        draw_texture(tile.tile_image, tile.x + (w * 16), tile.y + (h * 16), RAYWHITE)


            # Update the player's sprite location
            for player in self.players:
                #(Player Sprite, (player x + width offset - View), (player y + height offset))
                tempX = player.position[0]
                tempY = player.position[1]

                tempX += player.draw_width
                tempY += player.draw_height

                tempPosition = Vector2(tempX, tempY)

                draw_texture_rec(player.playerSprite, player.frame_rec, tempPosition, RAYWHITE)

            end_drawing()

            # Limits the frame rate of sprites (60 FPS walk cycle is bad)
            if get_time() > nextFrame:
                frame = (frame+1)%2
                superFrame = (superFrame+1)%3
                nextFrame += 60

    def clearGame(self):
        # Remove all player sprites 
        for player in self.players:
            unload_texture(player.playerSprite)
        # Remove all players from the player list
        self.players.clear()

        # Load the title screen
        self.gameIntro()

##########--END CLASSES--##########


#---------------------------------#


##########--BEGIN FUNCTIONS--######


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

game = Game()

game.gameIntro()

###########-End Main Code-#########