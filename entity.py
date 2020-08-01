########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that contains any entities                       #
########################################################################

# Note: This file is still a WIP, and --as such-- is not implemented yet!

# Entity class. All entities should inherit from this!
class Entity(object):
    def __init__(self, eType, xPos, yPos, width, height):
        self.type = eType
        self.xPos = xPos
        self.yPos = yPos
        self.position = [xPos, yPos]
        self.width = width
        self.height = height

    def physics(self):
        pass
        # Not looking forward to more physics ;-;

    # Returns true if the entity has made contact with the player, otherwise returns false
    def playerCollision(self, playerNumber, playerPos):
        playerX, playerY = playerPos

        # Check to see if the player is in range of the entity's hitbox
        if ( (((self.xPos + (self.width/2)) >= playerX) or ((self.xPos - (self.width/2)) <= playerX))\
            and (((self.yPos + (self.height/2)) >= playerY) or ((self.yPos - (self.height/2)) <= playerY))):
            return True
        else:
            return False

class BigStar(Entity):
    def __init__(self, eType, xPos = 0, yPos = 0, width = 0, height = 0, bigStarID = 0):
        # Inherit the Entitiy class and pass along our info
        super().__init__(eType, xPos, yPos, width, height)

    def collected(self):
        if self.playerCollision:
            pass


class Fireball(Entity):
    def __init__(self, eType, xPos = 0, yPos = 0, width = 0, height = 0, playerNumber):
        # Inherit the Entitiy class and pass along our info
        super().__init__(eType, xPos, yPos, width, height)
        self.playerNumber = playerNumber

    def fireCollision(self, player):

        #Function to make the other player drop a big star.
        if (self.playerNumber != player.playerNumber):
            pass

        # TODO: Make the fireball have physics and destroy on hitting a wall.

class Powerups(Entity):
    def __init__(self, eType, xPos = 0, yPos = 0, width = 0, height = 0, playerNumber, powerupID):
        # Inherit the Entitiy class and pass along our info
        super().__init__(eType, xPos, yPos, width, height)

        # Identifiers
        self.playerNumber = playerNumber
        self.powerupID = powerupID

        # Physics related
        self.gravity = 0
        self.velcoity = [0,0]
        self.position = [0,0]

    def powerupActor(self, powerupID):
        if powerupID == 0:
            pass