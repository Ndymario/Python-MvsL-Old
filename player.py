########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
#   Description: Player class/functions                                #
########################################################################

from pygame_functions import *
from level import *
SIZE = WIDTH, HEIGHT = 320, 240
wrap_around = True

# Define some in game constants (used for the Physics "engine")
FRICTION = 0.2
ACCELERATION = 0.1
GRAVITY = 2.5

class Player(object):
    def __init__(self, playerSprite = None, height = 0, weight = 0.2, player_number = 0, up = pygame.K_UP, down = pygame.K_DOWN, left = pygame.K_LEFT, right = pygame.K_RIGHT, x = 100, y = 100):
        # Keep track of the player number
        self.player_number = player_number

        # Used to determine what sprites to load for the player
        self.playerSprite = playerSprite

        # Player Positioning variables
        self.x = x
        self.y = y
        self.x_velocity = 0.00
        self.y_velocity = 0.00

        # Number is from height of the player sprite in pixles
        self.height = height

        # Define some physics related variables
        self.weight = weight
        self.SPEED_CAP = 6 
        self.VSPEED_CAP = -8
        self.DSPEED_CAP = 8

        # Define player controls
        self.up = up
        self.down = down
        self.left = left
        self.right = right

        # Define misc. Player variables
        self.last_held_direction = "right"
        self.idle = False
        self.skidding = False
    
    def gravity(self, gravity, level):
        p_weight = self.weight
        if ((self.y_velocity >= self.VSPEED_CAP) and (self.y_velocity < 0)):
            if p_weight <= gravity:
                    p_weight += gravity
                    
            else:
                p_weight = gravity

            self.y_velocity += (self.weight * p_weight)
            if self.y_velocity >= 0:
                self.y_velocity = 0.0

        elif((self.y_velocity >= 0.0) and (self.check_fall(level) ==False)):
            if p_weight <= gravity:
                p_weight += gravity
            else:
                p_weight = gravity

            self.y_velocity += (self.weight * p_weight)
            if self.y_velocity < self.VSPEED_CAP:
                self.y_velocity = self.VSPEED_CAP

        else:            
            if self.check_fall(level) != False:
                self.y_velocity = 0.0
                self.y = self.check_fall(level)
        if self.y_velocity > self.DSPEED_CAP:
                self.y_velocity = self.DSPEED_CAP
    
    # "Kill" the player when their y value >= 4000
    def death(self):
        if self.y >= 4000:
            self.respawn()

    # Really basic respawn function (set the players x & y pos. to 100)
    def respawn(self):
        self.x = 100
        self.y = 100

    # Check to see if the player can jump
    def check_jump(self,level):
        if level.tile_on(self.x, self.y) != False:
            return True
        return False

    # Check to see if the player should have gravity applied
    def check_fall(self,level):
        if level.tile_on(self.x,self.y) != False:
            return level.tile_on(self.x, self.y)
        return False

    def calculatePosition(self):
        # Make it so the player wraps around on the left and right (if enabled)
        if (wrap_around):
            if ((self.x >= WIDTH) and self.x_velocity >= 0):
                self.x = 1
            elif ((self.x <= 0) and (self.x_velocity <= 0)):
                self.x = WIDTH
        
        # Calculate the players next position using their coordinates
        # (This will probably be improved in the future)
        self.x += self.x_velocity
        self.y += self.y_velocity

    # Check if a player touches part of a tile
    def check_collision(self,level):
        if level.under_tile(self.x,self.y-20) != False:
            self.y = level.under_tile(self.x,self.y - 20)
            self.y_velocity = 0
            return

        if level.tile_on(self.x,self.y) != False and level.in_tile(self.x,self.y) == False:
            self.y = level.tile_on(self.x,self.y)
            self.y_velocity = 0
            return
        
        if level.in_tile(self.x,self.y) != False:
            if level.in_tile(self.x,self.y)[0] == False:
                self.x = level.in_tile(self.x,self.y)[1]
                self.x_velocity = 0
                return 
            else:
                self.y = level.in_tile(self.x,self.y)[1]
                self.y_velocity = 0
                return
        
        if level.in_tile(self.x,self.y-20) != False:
            if level.in_tile(self.x,self.y-20)[0] == True:
                self.y = level.in_tile(self.x,self.y-20)[1] + 20
                self.y_velocity = 0
                return 
            else:
                self.x = level.in_tile(self.x,self.y-20)[1]
                self.x_velocity = 0
                return                
        return
    
    # Make the player have friction against the ground
    def Friction(self):
        if ((self.x_velocity <= self.SPEED_CAP) and (self.x_velocity > 0)):
                if ((self.x_velocity <= self.SPEED_CAP) and (self.x_velocity > 0)):
                    self.x_velocity -= FRICTION
                    if self.x_velocity < 0:
                        self.x_velocity = 0.0
                else:
                    self.x_velocity = 0.0

        elif ((self.x_velocity >= -self.SPEED_CAP) and (self.x_velocity < 0)):
            if ((self.x_velocity >= -self.SPEED_CAP) and (self.x_velocity < 0)):
                    self.x_velocity += FRICTION
                    if self.x_velocity > 0:
                        self.x_velocity = 0.0
            else:
                self.x_velocity = 0.0

    # Calculate the player's horizontal velocity
    def HorizontalVelocity(self, last_held_direction, skidding, playerSprite):
        if (last_held_direction == "right"):
                # Cap the player's horizontal speed to the right
                if (self.x_velocity <= self.SPEED_CAP):
                    if (self.x_velocity < 0):
                        if (skidding == False):
                            # Update the player to their skidding animation when turning around
                            changeSpriteImage(playerSprite, 4*3)
                            skidding = True
                        else:
                            skidding = False
                    self.x_velocity += ACCELERATION
                    if self.x_velocity >= self.SPEED_CAP:
                        self.x_velocity = self.SPEED_CAP
                elif (self.x_velocity >= self.SPEED_CAP):
                    self.x_velocity = self.SPEED_CAP
        
        elif (last_held_direction == "left"):
                # Cap the player's horizontal speed to the left
                if (self.x_velocity >= -self.SPEED_CAP):
                    if (self.x_velocity > 0):
                        if (skidding == False):
                            # Update the player to their skidding animation when turning around
                            changeSpriteImage(playerSprite, 4*3+1)
                            skidding = True
                    else:
                        skidding = False
                    self.x_velocity -= ACCELERATION
                    if self.x_velocity <= -self.SPEED_CAP:
                        self.x_velocity = -self.SPEED_CAP
                elif (self.x_velocity <= -self.SPEED_CAP):
                    self.x_velocity = -self.SPEED_CAP

    # Calculate the players vertical velocity
    def VerticalVelocity(self):
        if (self.y_velocity > self.VSPEED_CAP):
            self.y_velocity = self.VSPEED_CAP
        elif (self.y_velocity < self.VSPEED_CAP):
            self.y_velocity = self.VSPEED_CAP

    # Allow the user to control the player
    def RefineInput(self, keys, level, playerSprite, frame):
        # Update the player's sprite when idling
        if (self.check_jump(level) == True):
            if (self.idle == False):
                # If the last input was to the right, face the Player's sprite to the right
                if (self.last_held_direction == "right"):
                    changeSpriteImage(playerSprite, 3*3+1)
                    updated = True
                # Otherwise, face Mario's sprite to the left
                else:
                    changeSpriteImage(playerSprite, 0*3+1)
                    updated = True

        # Set the last held direction to right, and update the player's walk animation if they're on the ground
        if keys[self.right]:
            self.last_held_direction = "right"

            # Check to see if the player is on the ground before applying the sprite change
            if (self.check_jump(level) == True):
                # Update the player's sprite when walking
                changeSpriteImage(playerSprite, 3*3+frame)

            self.HorizontalVelocity(self.last_held_direction, self.skidding, playerSprite)
    
        # Set the last held direction to left, and update the player's walk animation if they're on the ground           
        elif keys[self.left]:
            self.last_held_direction = "left"

            # Check to see if the player is on the ground before applying the sprite change
            if (self.check_jump(level) == True):
                # Update the player's sprite when walking
                changeSpriteImage(playerSprite, 0*3+frame)

            self.HorizontalVelocity(self.last_held_direction, self.skidding, playerSprite)
        
        elif keys[self.down]:
            # If the player is on the ground, make them duck
            if self.check_jump(level) == True:
                changeSpriteImage(playerSprite, 5*3 - 1)
            # Apply friction to the player
            self.Friction()
                
        # Apply friction to the player if they are not holding a button or ducking
        # (slow them to a hault)
        else:
            # Apply friction to the player
            self.Friction()

        # Check to see if the player can jump
        if keys[self.up]:
            if self.check_jump(level) == True:
                # If the last input was to the right, face the Player's sprite to the right
                if (self.last_held_direction == "right"):
                    changeSpriteImage(playerSprite, 2*3+frame)
                # Otherwise, face Mario's sprite to the left
                else:
                    changeSpriteImage(playerSprite, 1*3+frame)
                self.VerticalVelocity()

            else:
                # If the last input was to the right, face Mario's sprite to the right
                if (self.last_held_direction == "right"):
                    changeSpriteImage(playerSprite, 2*3+frame)
                # Otherwise, face Mario's sprite to the left
                else:
                    changeSpriteImage(playerSprite, 1*3+frame)
                # If the player can't jump, continue to apply gravity
                self.gravity(GRAVITY,level)

        # Apply gravity to the player
        elif (self.check_jump(level) == False):
            # If the last input was to the right, face Mario's sprite to the right
            if (self.last_held_direction == "right"):
                changeSpriteImage(playerSprite, 2*3+frame)
            # Otherwise, face Mario's sprite to the left
            else:
                changeSpriteImage(playerSprite, 1*3+frame)
            self.gravity(GRAVITY,level)

        else:
            self.gravity(GRAVITY,level)

    # Print stats of the player when called
    def __str__(self):
        return "Player X Velocity: {}\nPlayer Y Velocity: {}\nPlayer X: {}\nPlayer Y: {}"\
            .format(self.x_velocity, self.y_velocity, self.x, self.y)
