########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that defines the base entity class               #
########################################################################

class Entity:
    def __init__(self, sprites, entity_id, coordinates, spite_drawing_info, physics_info) -> None:
        # Keep track of this Entity's ID
        self.entity_id = entity_id

        # Keep track of the Entity's sprite information
        self.sprites = sprites
        self.sprite_drawing_info = spite_drawing_info

        # Keep track of the Entity's coordinates
        self.coodinates = coordinates

        # Keep track of the Entity's physics related properties (used for the physics engine)
        self.physics = physics_info

# Default coordinates template
coordinates = {
    "x": 0,
    "y": 0,
    "x velocity": 0,
    "y velocity": 0
}

# Default physics template
physics_info = {
    "weight": 0.2,
    "speed cap": 2,
    "top speed": 8,
    "air speed cap": 7.5,
    "acceleration": 0.05
}