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