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

class Game(object):
    def __init__(self):
        self.players = []

    def text_objects(self, text, font):
        text_surface = font.render(text, True, BLACK)
        return text_surface, text_surface.get_rect()

    def game_intro(self):
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
            large_text = pygame.font.Font('freesansbold.ttf', 100)
            text_surf, text_rect = self.text_objects("Mario vs Luigi", large_text)
            text_rect.center = ((800/2),(600/2))
            screen.blit(text_surf, text_rect)
            pygame.display.update()
            tick(15)
        
        # Run the game if the title screen is cleared
        self.game_loop()

    def game_loop(self):

        # Setup the screen and other display stuff
        # Note: WIDTH & HEIGHT are imported from player.py!
        screen = screenSize(WIDTH, HEIGHT, None, None, False)

        in_game = True

        # Load Level Data
        levelchunk1 = []

        # This recreates the collision map automatically
        cmap = CMap("Cmap/1-1.cmap")
        cmap.create_cmap("Levels/1-1.lvl")
        level = Level("Levels/1-1.lvl")

        # Frame handler (used for any sprite animation)
        frame = 0
        super_frame = 0
        next_frame = clock()

        # Create a player
        mario = Player("Sprites/Mario/")

        if P2: #Experimental 
            luigi = Player("Sprites/Luigi/", [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q, pygame.K_LSHIFT]\
                        , 1, 15, 100, 10, 20)
            self.players = [mario, luigi]
        else:
            self.players = [mario]
            
        # Load the Player's sprites
        for player in self.players:
            # The powerup handler already creates the player sprite, so use this to initalize the players
            player.powerup_handler(0)

        while in_game:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: sys.exit()
            keys = pygame.key.get_pressed()

            # Get player inputs
            for player in self.players:
                # Turn inputs into movement
                player.refine_input(keys, cmap, player.player_sprite, player.last_held_direction, frame, super_frame, level)        
            
                # Calculate and update position
                player.calculate_position()
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
                        mario.powerup_handler(0)
                        luigi.powerup_handler(0)

                    # Make both Bros. Super
                    if keys[pygame.K_1]:
                        mario.powerup_handler(1)
                        luigi.powerup_handler(1)
                    
                    # Make Mario Fire Mario
                    if keys[pygame.K_2]:
                        mario.powerup_handler(2)

                    # Return to the title screen
                    if keys[pygame.K_9]:
                        self.clear_game()
                
            # Limit the framerate to 60 FPS
            tick(60)

            #Render the screen
            screen.fill(WHITE)
            for tile in level.tiles:
                for w in range(int(tile.width / 16)):
                    for h in range(int(tile.height / 16)):
                        screen.blit(pygame.image.load(tile.tile_image), [tile.x + (w * 16), tile.y - (h * 16)])

            # Update the player's sprite location
            for player in self.players:
                moveSprite(player.player_sprite, player.x + player.draw_width, player.y + player.draw_height)

            updateDisplay()
            # Limits the frame rate of sprites (60 FPS walk cycle is bad)
            if clock() > next_frame:
                frame = (frame+1)%2
                super_frame = (super_frame+1)%3
                next_frame += 60

    def clear_game(self):
        # Remove all player sprites 
        for player in self.players:
            hideSprite(player.player_sprite)
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