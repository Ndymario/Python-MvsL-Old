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


# Probably doesn't need to be a class, and if it does, should probably be in a different file, but oh well
class Camera(object):
    def __init__(self):
        # Sets the camera position to player 0, originally planned to use a tuple for x and y but abandoned that
        self.camera = game.players[0].position[0]
        # Moving frames are used to control View position
        self.moving_frames = 0

        # Need to add y movement

    # Moves the View box (camera) around a player
    def move_view(self,player):
        # Defines when to stop adding onto the moving frames
        if self.moving_frames > 14:
            self.moving_frames = 14
        if self.moving_frames < -14:
            self.moving_frames = -14

        if self.moving_frames == 0:
            # Sets the camera to the middle of the screen
            tempX, tempY = player.position
            self.camera = tempX - 112
        else:
            # Moves the camera with the player
            tempX, tempY = player.position
            self.camera = tempX - 112 + (2 * self.moving_frames)

        # Defines the boundaries of how far the camera can go from the player, with the center being - 112
        if self.camera > player.position[0] - 84:
            self.camera = player.position[0] - 84
        elif self.camera < player.position[0] - 140:
            self.camera = player.position[0] - 140

class Game(object):
    def __init__(self):
        self.players = []

    def text_objects(self, text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    def game_intro(self):
        screen = screenSize(800, 600, None, None, False)

        intro = True

        while intro:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            if keys[pygame.K_SPACE]:
                intro = False
                    
            # Draws the title screen
            screen.fill(WHITE)
            largeText = pygame.font.Font('freesansbold.ttf', 100)
            TextSurf, TextRect = self.text_objects("Mario vs Luigi", largeText)
            TextRect.center = ((800/2),(600/2))
            screen.blit(TextSurf, TextRect)
            pygame.display.update()
            tick(15)
        
        # Run the game if the title screen is cleared
        self.gameLoop()

    def gameLoop(self):

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
                        , 1, 10, 20)
            self.players = [mario, luigi]
        else:
            self.players = [mario]

        old_x = self.players[0].position[0]

        View = Camera()
            
        # Load the Player's sprites
        for player in self.players:
            # The powerup handler already creates the player sprite, so use this to initalize the players
            player.powerupHandler(0)

        while inGame:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: sys.exit()
            keys = pygame.key.get_pressed()

            # Get player inputs
            for player in self.players:
                # Turn inputs into movement
                player.RefineInput(keys, cmap, player.playerSprite, player.last_held_direction, frame, superFrame, level)        
            
                # Calculate and update position

                player.calculatePosition(10, cmap)
                updated_position = player.check_collision(cmap)
                player.position = (updated_position[0], updated_position[1])
                player.velocity = (updated_position[2], updated_position[3])

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
                        self.clearGame()

            # Detect if player moved
            if round(self.players[0].position[0]) > old_x:
                # If player moved to the right, try to move the View a bit
                View.moving_frames += .5
            elif round(self.players[0].position[0]) < old_x:
                # If player moved to the left, try to move the View a bit
                View.moving_frames -= .5

            # Used to detect a change in x between each frame to control View
            old_x = round(self.players[0].position[0])

            # Move the View box
            View.move_view(self.players[0])

            # Limit the framerate to 60 FPS
            tick(60)

            #Render the screen
            screen.fill(WHITE)
            for tile in level.tiles:
                for w in range(int((tile.width) / 16)):
                    for h in range(int(tile.height / 16)):
                        # (Image to load, [(left coord of tile * width) - View, (bottom coord of tile - height)])
                        screen.blit(pygame.image.load(tile.tile_image), [tile.x + (w * 16) - View.camera, tile.y - (h * 16)])

            # Update the player's sprite location
            for player in self.players:
                # (Player Sprite, (player x + width offset - View), (player y + height offset))
                moveSprite(player.playerSprite, round(player.position[0]) + player.draw_width - View.camera, player.position[1] + player.draw_height)

            updateDisplay()
            # Limits the frame rate of sprites (60 FPS walk cycle is bad)
            if clock() > nextFrame:
                frame = (frame+1)%2
                superFrame = (superFrame+1)%3
                nextFrame += 60

    def clearGame(self):
        # Remove all player sprites 
        for player in self.players:
            hideSprite(player.playerSprite)
        # Remove all players from the player list
        self.players.clear()

        # Load the title screen
        self.game_intro()

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

game.game_intro()

###########-End Main Code-#########