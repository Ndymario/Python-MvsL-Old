########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that contains any entities                       #
########################################################################

class Fireball(object):
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber

    def playerCollision(self, player):

        #Function to make the other player drop a big star.
        if (self.playerNumber != player.playerNumber):
            pass

        # TODO: Make the fireball have physics and destroy on hitting a wall.