########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that handles the animation controller            #
########################################################################

class AnimationController():

    # Function that will handle updating the passed entity's sprite for the next frame
    # Ex: Changing from frame 1 of "walking" to frame 2 of "walking"
    def update_frame(self, entity):
        pass

    # Function that will handle upating the entity's sptite "state"
    # Ex: Changing from "idle" to "walking"
    def update_sprite(self, entity, new_sprite):
        pass

    # Function that will handle upating the entity's sptite sheet
    # Ex: Changing from "small" to "super"
    def update_sprite_sheet(self, entity, new_sheet):
        pass