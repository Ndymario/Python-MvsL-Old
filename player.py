########################################################################
#   Author: Nolan Y.                                                   #
#                                                                      #
#   Description: Player class/functions                                #
########################################################################

from level import *
SIZE = WIDTH, HEIGHT = 320, 240
wrap_around = True

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
        self.VSPEED_CAP = -8
    
    def gravity(self, gravity):
        p_weight = self.weight
        if ((self.y_velocity >= self.VSPEED_CAP) and (self.y_velocity < 0)):
            if p_weight <= gravity:
                    p_weight += gravity
                    
            else:
                p_weight = gravity
            self.y_velocity += (self.weight * p_weight)

            if self.y_velocity >= 0:
                self.y_velocity = 0.0

        elif((self.y_velocity >= 0.0) and (self.check_fall() ==False)):
            if p_weight <= gravity:
                p_weight += gravity
            else:
                p_weight = gravity

            self.y_velocity += (self.weight * p_weight)
            if self.y_velocity < self.VSPEED_CAP:
                self.y_velocity = self.VSPEED_CAP

        else:
            if self.check_fall() != False:
                self.y_velocity = 0.0
                self.y = self.check_fall()
    
    def death(self):
        pass

    def respawn(self):
        pass
    
    def check_jump(self):
        for i in range(len(levelchunk1)):
            if (self.y == levelchunk1[i-1].top) and self.x <= levelchunk1[i-1].width + levelchunk1[i-1].x and self.x >=levelchunk1[i-1].x - levelchunk1[i-1].x: 
                return True
        return False

    def check_fall(self):
        for i in range(len(levelchunk1)):
            if (self.y >= levelchunk1[i-1].top) and self.y <= levelchunk1[i-1].top + 10 and self.x <= levelchunk1[i-1].width + levelchunk1[i-1].x and self.x >=levelchunk1[i-1].x - 16: 
                return levelchunk1[i-1].top
        return False

    # Check to see if the player can jump
    def check_jump(self):
        for i in range(len(levelchunk1)):
            if (self.y == levelchunk1[i-1].top) and self.x <= levelchunk1[i-1].width + levelchunk1[i-1].x\
                and self.x >=levelchunk1[i-1].x - levelchunk1[i-1].x: 
                return True
        return False

    # Check to see if the player should have gravity applied
    def check_fall(self):
        for i in range(len(levelchunk1)):
            if (self.y >= levelchunk1[i-1].top) and self.y <= levelchunk1[i-1].top + 10\
                and self.x <= levelchunk1[i-1].width + levelchunk1[i-1].x and self.x >=levelchunk1[i-1].x - 15: 
                return levelchunk1[i-1].top
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

    
    # Print stats of the player when called
    def __str__(self):
        return "Player X Velocity: {}\nPlayer Y Velocity: {}\nPlayer X: {}\nPlayer Y: {}"\
            .format(self.x_velocity, self.y_velocity, self.x, self.y)