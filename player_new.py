########################################################################
#   Author: Nolan Y.                                                   #
#   Description: Re-write the player classes/functions                 #
########################################################################

from entity import Entity

class Player(Entity):
    def __init__(self, sprites, entity_id, coordinates, spite_drawing_info, physics_info, controls) -> None:
        super().__init__(sprites, entity_id, coordinates, spite_drawing_info, physics_info)

        # Keep tack of the player's preferred control scheme and other control related variables
        self.controls = controls
        self.released_up = True
        self.sprinting = False

        # Keep track of the player's powerup state
        self.powerup_state = 0

    def __str__(self) -> str:
        return super().__str__() + "\nPower Up State: {0}\nReleased Up: {1}\nIs Sprinting: {2}".format(self.powerup_state, self.released_up, self.sprinting)