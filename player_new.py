########################################################################
#   Author: Nolan Y.                                                   #
#   Description: Re-write the player classes/functions                 #
########################################################################

from animation_controller import AnimationController
from entity import Entity

class Player(Entity):
    def __init__(self, sprites, entity_id, coordinates, sprite_sheets, spite_drawing_info, sprite_sheet_info, physics_info, animation_controller, controls) -> None:
        super().__init__(sprites, entity_id, coordinates, sprite_sheets, spite_drawing_info, physics_info, sprite_sheet_info, animation_controller)

        # Keep tack of the player's preferred control scheme and other control related variables
        self.controls = controls
        self.released_up = True
        self.sprinting = False

        # Keep track of the player's powerup state
        self.powerup_state = 0

        # Variables for Dicionary Keys
        self.width = "width"
        self.height = "height"
        self.draw_width = "draw width"
        self.draw_height = "draw height"

    def __str__(self) -> str:
        return super().__str__() + "\nPower Up State: {0}\nReleased Up: {1}\nIs Sprinting: {2}".format(self.powerup_state, self.released_up, self.sprinting)

    def powerup_handler(self, powerup_id):
        # 0 - Small
        # 1 - Super
        # 2 - Fire Flower
        # 3 - Blue Shell
        # 4 - Mini Mushroom
        # 5 - Mega Mushroom
        # 6 - Hammer Suit
        # 7 - Frog Suit
        # 8 - Raccoon Leaf
        # 9 - Cape Feather
        # 10 - Propeller Suit
        # 11 - Mari0 (Portal Gun + Mario)

        # Change the player's powerup state to the coorect powerup ID
        self.powerup_state = powerup_id

        # Load the correct spritesheet depending on the powerup
        if (powerup_id == 0):
            self.powerup_state = 0
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["small"])

        elif (powerup_id == 1):
            self.powerup_state = 1
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["super"])

        elif (powerup_id == 2):
            self.powerup_state = 2
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["fire"])
        
        elif (powerup_id == 3):
            self.powerup_state = 3
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["shell"])
        
        elif (powerup_id == 4):
            self.powerup_state = 4
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["mini"])
        
        elif (powerup_id == 5):
            self.powerup_state = 5
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["mega"])
        
        elif (powerup_id == 6):
            self.powerup_state = 6
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["hammer"])
        
        elif (powerup_id == 7):
            self.powerup_state = 7
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["frog"])
        
        elif (powerup_id == 8):
            self.powerup_state = 8
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["raccoon"])
        
        elif (powerup_id == 9):
            self.powerup_state = 9
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["cape"])

        elif (powerup_id == 10):
            self.powerup_state = 10
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["propeller"])
        
        elif (powerup_id == 11):
            self.powerup_state = 11
            self.animation_controller.update_sprite_sheet(self, self.sprite_sheet_info["portal"])

# Example controls dict
controls = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "jump": pygame.K_SPACE,
    "sprint": pygame.K_RSHIFT
}

# Example sprite info dict
small = {
    # Key is the animation name
    # Value is what is passed to the sprite controller.
    #   First index is the file path, second index is first sprite to use
    #   Second index is the ending sprite (defaults to None)
    "idle": ["Sprites/Mario/small.png", 0],
    "walk": ["Sprites/Mario/small.png", 1, 3],
    "sprint": ["Sprites/Mario/small.png", 4, 6],
    "jump": ["Sprites/Mario/small.png", 7],
    "skidding": ["Sprites/Mario/small.png", 8]
}

# Example sprite sheet info dict
sprite_sheet_info = {
    # Key is the "bundle" id.
    #   Ex: Small is for all sprites that deal with small Mario
    # Value is the sprite info
    "small": small
}