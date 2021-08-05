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

    def __str__(self) -> str:
        return "Entity ID: {0}\nEntity X-Cord: {1}\nEntity X-Cord: {2}\nEntity X-Cord: {3}\nEntity X-Cord: {4}\
            \nEntity X-Cord: {5}\nEntity X-Cord: {6}".format(self.entity_id, self.coodinates["x"], self.coodinates["y"]\
            , self.coodinates["x velocity"], self.coodinates["y velocity"], self.coodinates["facing"], self.coodinates["skidding"])

# Default coordinates template
coordinates = {
    "x": 0,
    "y": 0,
    "x velocity": 0,
    "y velocity": 0,
    "facing": "right",
    "skidding": False
}

# Default physics template
physics_info = {
    "weight": 0.2,
    "speed cap": 2,
    "top speed": 8,
    "air speed cap": 7.5,
    "acceleration": 0.05
}

