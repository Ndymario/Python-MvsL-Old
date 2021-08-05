########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that handles all physics related calculations    #
########################################################################

class Physics(object):
    def __init__(self, cmap, level_info, animation_controller):
        # Define what collision map to use in the calculations
        self.cmap = cmap

        # Define what animation controller to use
        self.animation_controller = animation_controller

        # Define a global gravity variable
        self.gravity = 2.8

        # Define constants for this instance of the physics engines
        self.level_info = level_info

        # Define variables for the Dicionary Keys
        #   Coordinate keys
        self.weight = "weight"
        self.scap = "speed cap"
        self.tspeed = "top speed"
        self.ascap = "air speed cap"
        self.accel = "acceleration"
        self.x = "x"
        self.y = "y"
        self.x_vel = "x velocity"
        self.y_vel = "y velocity"
        self.direction = "facing"
        self.skidding = "skidding"

        #   Level info keys
        self.lvl_width = "level width"
        self.lvl_height = "level height"
        self.wrap = "level wrap"
        self.friction_level = "friction"

    # Function to calculate gravity for the passed entity
    def gravity(self, *entity):
        for entity in entity:
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
                if (self.check_fall(entity) != False):
                    entity.coordinates[self.y_vel] = 0.0
                    entity.coordinates[self.y] = self.check_fall(entity)[1]

            if (entity.coordinates[self.y_vel] > (-1 * entity.physics_info[self.ascap])):
                entity.coordinates[self.y_vel] = (-1 * entity.physics_info[self.ascap])

    # Check if an entity should have gravity applied to them
    def check_fall(self, entity):
        if self.cmap.on_tile(entity.coordinates[self.x],entity.coordinates[self.y],self.width,self.height) != False:
            return self.cmap.on_tile(entity.coordinates[self.x], entity.coordinates[self.y], self.width, self.height)
        return False

    def calculate_position(self, *entity):
        for entity in entity:
            # Make it so the entity wraps around on the left and right (if enabled)
            if (self.level_info[self.wrap]):
                if ((entity.coordinates[self.x] >= self.level_info[self.lvl_width]) and entity.coordinates[self.x_vel] >= 0):
                    entity.coordinates[self.x] = 1
                elif ((entity.coordinates[self.x] <= 0) and (entity.coordinates[self.x_vel] <= 0)):
                    entity.coordinates[self.x] = self.level_info[self.lvl_width]
        
            # Calculate the players next position using their coordinates
            # (This will probably be improved in the future)
            entity.coordinates[self.x] += entity.coordinates[self.x_vel]
            entity.coordinates[self.y] += entity.coordinates[self.y_vel]

    # Check if an entity is touching part of a tile
    def check_collision(self, cmap, *entity):
        for entity in entity:
            if entity.coordinates[self.y] >= self.level_info[self.lvl_height]:
                return entity.coordinates[self.x], entity.coordinates[self.y], entity.coordinates[self.x_velocity], entity.coordinates[self.y_velocity], False
            return cmap.in_tile(entity.coordinates[self.x], entity.coordinates[self.y], entity.coordinates[self.x_velocity], entity.coordinates[self.y_velocity], self.level_info[self.width], self.level_info[self.height])

    # Make the entity have friction along the ground
    def friction(self, *entity):
        for entity in entity:
            if ((entity.coordinates[self.x_vel] <= entity.physics_info[self.scap]) and (entity.coordinates[self.x_vel] > 0)):
                    if ((entity.coordinates[self.x_vel] <= entity.physics_info[self.scap]) and (entity.coordinates[self.x_vel] > 0)):
                        entity.coordinates[self.x_vel] -= self.level_info[self.friction_level]
                        if (entity.coordinates[self.x_vel] < 0):
                            entity.coordinates[self.x_vel] = 0.0
                    else:
                        entity.coordinates[self.x_vel] = 0.0

            elif ((entity.coordinates[self.x_vel] >= -entity.physics_info[self.scap]) and (entity.coordinates[self.x_vel] < 0)):
                if ((entity.coordinates[self.x_vel] >= -entity.physics_info[self.scap]) and (entity.coordinates[self.x_vel] < 0)):
                        entity.coordinates[self.x_vel] += self.level_info[self.friction_level]
                        if (entity.coordinates[self.x_vel] > 0):
                            entity.coordinates[self.x_vel] = 0.0
                else:
                    entity.coordinates[self.x_vel] = 0.0

    def horizontal_velocity(self, *entity):
        for entity in entity:
            if (entity.coordinates[self.direction] == "right"):
                # Cap the entity's horizontal speed to the right
                if (entity.coordinates[self.x_vel] <= entity.physiscs_info[self.scap]):
                    if (entity.coordinats[self.x_vel] < -0.5):
                        if (not entity.coordinates[self.skidding]):
                            self.animation_controller.update_sprite(entity.sprite["skidding left"])
                            entity.coordinates[self.skidding] = True
                        
                    else:
                        entity.coordinates[self.skidding] = False
                    
                    if (entity.coordinates[self.skidding]):
                        entity.coordinates[self.x_vel] += entity.phyisics_info[self.accel] * 2

                    else:
                        entity.coordinates[self.x_vel] += entity.phyisics_info[self.accel]
                    
                    if (entity.coordinates[self.x_vel] > entity.phyisics_info[self.scap]):
                        self.friction(entity)
                
                elif (entity.coordinates[self.x_vel] > entity.phyisics_info[self.scap]):
                    self.friction(entity)

            if (entity.coordinates[self.direction] == "left"):
                # Cap the entity's horizontal speed to the right
                if (entity.coordinates[self.x_vel] >= -entity.physiscs_info[self.scap]):
                    if (entity.coordinats[self.x_vel] > 0.5):
                        if (not entity.coordinates[self.skidding]):
                            self.animation_controller.update_sprite(entity.sprite["skidding left"])
                            entity.coordinates[self.skidding] = True
                        
                    else:
                        entity.coordinates[self.skidding] = False
                    
                    if (entity.coordinates[self.skidding]):
                        entity.coordinates[self.x_vel] -= entity.phyisics_info[self.accel] * 2

                    else:
                        entity.coordinates[self.x_vel] -= entity.phyisics_info[self.accel]
                    
                    if (entity.coordinates[self.x_vel] <= -entity.phyisics_info[self.scap]):
                        self.friction(entity)
                
                elif (entity.coordinates[self.x_vel] <= -entity.phyisics_info[self.scap]):
                    self.friction(entity)

    # Cap the entity's vertical velocity
    def vertical_velocity(self, *entity):
        for entity in entity:
            if (entity.coordinates[self.y_vel] > self.ascap):
                entity.coordinates[self.y_vel] = self.VSPEED_CAP

            elif (entity.coordinates[self.y_vel] < self.ascap):
                entity.coordinates[self.y_vel] = -self.VSPEED_CAP
