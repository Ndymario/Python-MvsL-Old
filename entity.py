########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that contains any entities                       #
########################################################################

# Note: This file is still a WIP, and --as such-- is not implemented yet!

# Entity class. All entities should inherit from this!
class Entity(object):
    def __init__(self, eType, xPos = 0, yPos = 0, width = 0, height = 0):
        self.type = eType
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height

    def playerCollision(self, playerNumber, playerPos):
        playerX, playerY = playerPos

        # Check to see if the player is in range of the entity's hitbox
        if ( (((self.xPos + (self.width/2)) >= playerX) or ((self.xPos - (self.width/2)) <= playerX))\
            and (((self.yPos + (self.height/2)) >= playerY) or ((self.yPos - (self.height/2)) <= playerY))):
            return True
        else:
            return False

class BigStar(Entity):
    def __init__(self):
        Entity.__init__("Big Star")

class Fireball(Entity):
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber

    def playerCollision(self, player):

        #Function to make the other player drop a big star.
        if (self.playerNumber != player.playerNumber):
            pass

        # TODO: Make the fireball have physics and destroy on hitting a wall.

class Powerups(Entity):
    def __init__(self, playerNumber):
        # Identifiers
        self.playerNumber = playerNumber
        self.powerupID = powerupID

        # Physics related
        self.gravity = 0

    def powerupActor(self, powerupID):
        if powerupID == 0:
            pass