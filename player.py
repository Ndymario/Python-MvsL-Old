########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #                                                                      #
#   Description: Player class/functions                                #
########################################################################

from pygame_functions import *
from level import *
SIZE = WIDTH, HEIGHT = 320, 240
wrap_around = True

# Define some in game constants (used for the Physics "engine")
FRICTION = .2
ACCELERATION = 0.1
V_ACCELERATION = 0.1
GRAVITY = 2.5

class Player(object):
    def __init__(self, skin = None, height = 0, weight = 0.2, player_number = 0):
        self.player_number = player_number
        # Used to determine what sprites to load for the player
        self.skin = skin
        self.x = 100
        self.y = 100
        self.x_velocity = 0.00
        self.y_velocity = 0.00
        # Number is from height of the player sprite in pixles
        self.height = height
        self.weight = weight
        self.SPEED_CAP = 8 
        self.VSPEED_CAP = -8
        self.DSPEED_CAP = 8
    
    def gravity(self, gravity,level):
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
    
    def death(self):
        pass

    def respawn(self):
        pass


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
            if (((self.x >= WIDTH - 10) and (self.x <= WIDTH)) and self.x_velocity >= 0):
                self.x = 11
            elif ((self.x >= 0) and (self.x <= 10)) and (self.x_velocity <= 0):
                self.x = WIDTH - 11
        
        # Calculate the players next position using their coordinates
        # (This will probably be improved in the future)
        self.x += self.x_velocity
        self.y += self.y_velocity

    # Check if player touches part of a tile
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

    def VerticalVelocity(self):
        if (self.y_velocity > self.VSPEED_CAP):
            self.y_velocity = self.VSPEED_CAP
        elif (self.y_velocity < self.VSPEED_CAP):
            self.y_velocity = self.VSPEED_CAP


    # Print stats of the player when called
    def __str__(self):
        return "Player X Velocity: {}\nPlayer Y Velocity: {}\nPlayer X: {}\nPlayer Y: {}"\
            .format(self.x_velocity, self.y_velocity, self.x, self.y)
