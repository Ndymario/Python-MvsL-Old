########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that contains any entities                       #
########################################################################

# Note: This file is still a WIP, and -- as such -- is not implemented yet!
class Fireball(object):
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber

    def playerCollision(self, player):

        #Function to make the other player drop a big star.
        if (self.playerNumber != player.playerNumber):
            pass

        # TODO: Make the fireball have physics and destroy on hitting a wall.

class Powerups(object):
    def __init__(self, playerNumber):
        # Identifiers
        self.playerNumber = playerNumber
        self.powerupID = powerupID

        # Physics related
        self.gravity = 0

    def powerupActor(self, powerupID):
        if powerupID == 0:
            pass