########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that handles all physics related calculations    #
########################################################################

class Physics(object):
    def __init__(self, cmap):
        # Define what collision map to use in the calculations
        self.cmap = cmap

        # Define a global gravity variable
        self.gravity = 2.8

        # Define variables for the Dicionary Keys
        self.weight = "weight"
        self.scap = "speed cap"
        self.tspeed = "top speed"
        self.ascap = "air speed cap"
        self.accel = "acceleration"
        self.x = "x"
        self.y = "y"
        self.x_vel = "x velocity"
        self.y_vel = "y velocity"

    # Function to calculate gravity for the passed entity
    def gravity(self, entity):

        # If the entity is in the air, apply incremenal gravity
        if((entity.coordinates[self.y_vel] >= entity.physics_info[self.ascap]) and (entity.coordinates[self.y_vel]) < 0):
            if (entity.physics_info[self.weight]):
                entity.physics_info[self.weight] += self.gravity

            else:
                entity.physics_info[self.weight] = self.gravity

            entity.coordinates[self.y_vel] += (entity.physics_info[self.weight] * entity.physics_info[self.weight])

            if(entity.coordinates[self.y_vel] >= 0.0):
                entity.coordinates[self.y_vel] = 0.0

        elif((entity.coordinates[self.y_vel] >= 0.0) and (self.check_fall(self.cmap) == False)):
            if (entity.physics_info[self.weight] <= self.gravity):
                entity.physics_info[self.weight] += self.gravity

            else:
                entity.physics_info[self.weight] = self.gravity

            entity.coordinates[self.y_vel] += (entity.physics_info[self.weight] * entity.physics_info[self.weight])

            if(entity.coordinates[self.y_vel] >= 0.0):
                entity.coordinates[self.y_vel] = 0.0

        else:
            if (self.check_fall(self.cmap) != False):
                entity.coordinates[self.y_vel] = 0.0
                entity.coordinates[self.y] = self.check_fall(self.cmap)[1]

        if (entity.coordinates[self.y_vel] > (-1 * entity.physics_info[self.ascap])):
            entity.coordinates[self.y_vel] = (-1 * entity.physics_info[self.ascap])
