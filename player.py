########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #
#   Description: Player class/functions                                #
########################################################################

from pygame_functions import *
from level import *
from cmap import *
SIZE = WIDTH, HEIGHT = 256, 192
wrap_around = True

# Define some in game constants (used for the Physics "engine")
FRICTION = 0.2
GRAVITY = 2.8

# Create player sound effects
jump = makeSound("Sounds/jump.wav")

class Player(object):
    def __init__(self, playerSprites = None, controls = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RSHIFT]\
                 , player_number = 0, x = 50, y = 100, width = 10, height = 20, draw_width = 4, draw_height = -13):
        # Keep track of the player number
        self.player_number = player_number

        # Used to determine what sprites to load for the player
        self.playerSprite = None
        self.playerSprites = playerSprites

        # Player Positioning variables
        self.x = x
        self.y = y
        self.x_velocity = 0.00
        self.y_velocity = 0.00

        # Number is from height/width of the player sprite in pixles
        self.width = width
        self.height = height

        # Number is how far from (x,y) coordinates to draw sprite because dumb
        self.draw_width = draw_width
        self.draw_height = draw_height

        # Define some physics related variables
        self.weight = 0.2
        self.SPEED_CAP = 2
        self.MAX_SPEED_CAP = 8
        self.VSPEED_CAP = -7.5
        self.DSPEED_CAP = 7.5
        self.ACCELERATION = 0.05

        # Define player controls
        self.controls = controls
        self.up = controls[0]
        self.down = controls[1]
        self.left = controls[2]
        self.right = controls[3]
        self.sprint = controls[4]

        # Define misc. Player variables
        self.last_held_direction = "right"
        self.idle = False
        self.skidding = False
        self.initalized = False

        # Powerup state for the player
        self.powerupState = 0
        self.released_up = True
        self.sprinting = False
    
    def gravity(self, gravity, level, cmap):
        p_weight = self.weight
        if ((self.y_velocity >= self.VSPEED_CAP) and (self.y_velocity < 0)):
            if p_weight <= gravity:
                    p_weight += gravity
                    
            else:
                p_weight = gravity

            self.y_velocity += (self.weight * p_weight)
            if self.y_velocity >= 0:
                self.y_velocity = 0.0

        elif((self.y_velocity >= 0.0) and (self.check_fall(cmap) ==False)):
            if p_weight <= gravity:
                p_weight += gravity
            else:
                p_weight = gravity

            self.y_velocity += (self.weight * p_weight)
            if self.y_velocity < self.VSPEED_CAP:
                self.y_velocity = self.VSPEED_CAP

        else:            
            if self.check_fall(cmap) != False:
                self.y_velocity = 0.0
                self.y = self.check_fall(cmap)[1]

        if self.y_velocity > self.DSPEED_CAP:
                self.y_velocity = self.DSPEED_CAP

    # Used to determine what sprite to use for each animation
    # (Not all spritesheets will be layed out the same!)
    def animationController(self, action, last_held_direction, frame = 0, superFrame = 0):
        # Sprites for powerup state 0
        if (self.powerupState == 0):
            if (action == "idle"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 13)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 0)

            elif (action == "jump"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 9)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 4)
            
            elif (action == "fall"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 8)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 5)

            elif (action == "walk"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 13 - frame)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 0 + frame)

            elif (action == "run"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 11 - frame)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 2 + frame)

            elif (action == "skidding"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 14)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 15)
            
            elif (action == "duck"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 17)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 16)

        elif (self.powerupState  == 1):
            if (action == "idle"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 17)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 0)
            
            elif (action == "jump"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 11)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 6)
            
            elif (action == "fall"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 10)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 7)

            elif (action == "walk"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 17 - superFrame)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 0 + superFrame)
            
            elif (action == "run"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 14 - superFrame)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 3 + superFrame)
            
            elif (action == "skidding"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 18)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 19)
            
            elif (action == "duck"):
                if (last_held_direction == "right"):
                    changeSpriteImage(self.playerSprite, 21)
                elif (last_held_direction == "left"):
                    changeSpriteImage(self.playerSprite, 20)

    def spriteChanger(self, newSprite, frames):
        if (self.playerSprite != None):
            hideSprite(self.playerSprite)
        self.playerSprite = makeSprite(newSprite, frames)
        showSprite(self.playerSprite)
    
    def powerupHandler(self, powerupID):
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

        # Change the player's powerup state to the coorect powerup ID
        self.powerupState = powerupID

        # Load the correct spritesheet depending on the powerup
        if (powerupID == 0):
            self.powerupState = 0

            if (self.player_number == 0):
                self.draw_height  = -21
                self.height = 15
            elif (self.player_number == 1):
                self.draw_height  = -23
                self.height = 15
            
            spriteSheet = self.playerSprites + "small.png"
            self.spriteChanger(spriteSheet, 18)
            return spriteSheet

        elif (powerupID == 1):
            self.powerupState = 1

            if (self.player_number == 0):
                self.draw_height  = -30
                self.height = 27
            elif (self.player_number == 1):
                self.draw_height  = -30
                self.height = 20

            spriteSheet = self.playerSprites + "super.png"
            self.spriteChanger(spriteSheet, 22)
            return spriteSheet
    
    # If the player gets hurt, make them shrink one powerup, otherwise kill the player
    def hurt(self):
        if (self.powerupState > 1):
            self.draw_height = -18
            self.height = 20
            self.powerupState = 1
            self.powerupHandler(1)

        elif (self.powerupState == 1):
            self.powerupState = 0
            self.draw_height  = -13
            self.height = 26
            self.powerupHandler(0)

        elif (self.powerupState == 0):
            self.respawn()

    # "Kill" the player when their y value >= 4000
    def death(self):
        if self.y >= HEIGHT:
            self.respawn()

    # Really basic respawn function (set the players x & y pos. to 100)
    def respawn(self):
        self.x = 100
        self.y = 100
        self.x_velocity = 0
        self.y_velocity = 0

    # Check to see if the player can jump
    def check_jump(self,cmap):
        if cmap.on_tile(self.x,self.y,self.width,self.height) != False:
            return True
        return False

    # Check to see if the player should have gravity applied
    def check_fall(self,cmap):
        if cmap.on_tile(self.x,self.y,self.width,self.height) != False:
            return cmap.on_tile(self.x, self.y,self.width,self.height)
        return False

    def calculatePosition(self):
        # Make it so the player wraps around on the left and right (if enabled)
        if (wrap_around):
            if ((self.x >= WIDTH) and self.x_velocity >= 0):
                self.x = 1
            elif ((self.x <= 0) and (self.x_velocity <= 0)):
                self.x = WIDTH
        
        # Calculate the players next position using their coordinates
        # (This will probably be improved in the future)
        self.x += self.x_velocity
        self.y += self.y_velocity

    # Check if a player touches part of a tile
    def check_collision(self, cmap):
        if self.y >= HEIGHT:
            return self.x,self.y,self.x_velocity,self.y_velocity,False
        return cmap.in_tile(self.x,self.y,self.x_velocity,self.y_velocity,self.width,self.height)
            
    # Make the player have friction against the ground
    def Friction(self):
        if ((self.x_velocity <= self.MAX_SPEED_CAP) and (self.x_velocity > 0)):
                if ((self.x_velocity <= self.MAX_SPEED_CAP) and (self.x_velocity > 0)):
                    self.x_velocity -= FRICTION
                    if self.x_velocity < 0:
                        self.x_velocity = 0.0
                else:
                    self.x_velocity = 0.0

        elif ((self.x_velocity >= -self.MAX_SPEED_CAP) and (self.x_velocity < 0)):
            if ((self.x_velocity >= -self.MAX_SPEED_CAP) and (self.x_velocity < 0)):
                    self.x_velocity += FRICTION
                    if self.x_velocity > 0:
                        self.x_velocity = 0.0
            else:
                self.x_velocity = 0.0

    # Calculate the player's horizontal velocity
    def HorizontalVelocity(self, last_held_direction, skidding, playerSprite):
        if (last_held_direction == "right"):
                # Cap the player's horizontal speed to the right
                if (self.x_velocity <= self.SPEED_CAP):
                    if (self.x_velocity < -0.5):
                        if (skidding == False):
                            # Update the player to their skidding animation when turning around
                            self.animationController("skidding", last_held_direction)
                            skidding = True
                    else:
                        skidding = False

                    if (skidding == True):
                        self.x_velocity += self.ACCELERATION  * 2
                        
                    else:
                        self.x_velocity += self.ACCELERATION
                    if self.x_velocity >= self.SPEED_CAP:
                        self.x_velocity = self.SPEED_CAP
                elif (self.x_velocity >= self.SPEED_CAP):
                    self.x_velocity = self.SPEED_CAP
        
        elif (last_held_direction == "left"):
                # Cap the player's horizontal speed to the left
                if (self.x_velocity >= -self.SPEED_CAP):
                    if (self.x_velocity > 0.5):
                        if (skidding == False):
                            # Update the player to their skidding animation when turning around
                            self.animationController("skidding", last_held_direction)
                            skidding = True
                    else:
                        skidding = False
                    
                    if (skidding == True):
                        self.x_velocity -= self.ACCELERATION  * 2
                        
                    else:
                        self.x_velocity -= self.ACCELERATION

                    if self.x_velocity <= -self.SPEED_CAP:
                        self.Friction()
                elif (self.x_velocity <= -self.SPEED_CAP):
                    self.Friction()

    # Calculate the players vertical velocity
    def VerticalVelocity(self):
        if (self.y_velocity > self.VSPEED_CAP):
            self.y_velocity = self.VSPEED_CAP
        elif (self.y_velocity < self.VSPEED_CAP):
            self.y_velocity = self.VSPEED_CAP

    # Allow the user to control the player
    def RefineInput(self, keys, cmap, playerSprite, last_held_direction, frame, superFrame, level):
        # Update the player's sprite when idling
        if (self.check_jump(cmap) == True):
            if (self.idle == False):
                self.animationController("idle", last_held_direction, frame, superFrame)

        # Set the last held direction to right, and update the player's walk animation if they're on the ground
        if keys[pygame.K_z]:
            print(self.y)
            
        if keys[self.sprint]:
            self.SPEED_CAP = 4
            self.ACCELERATION = 0.075
        else:
            self.SPEED_CAP = 2
            self.ACCELERATION = .07
        
        if keys[self.right]:
            self.last_held_direction = "right"

            # Check to see if the player is on the ground before applying the sprite change
            if (self.check_jump(cmap) == True):
                # Check to see if ducking
                if keys[self.down]:
                    self.animationController("duck", last_held_direction, frame, superFrame)
                    self.Friction()
                else:
                    # Update the player's sprite when walking
                    if (self.x_velocity <= 2):
                        self.animationController("walk", last_held_direction, frame, superFrame)
                    # Update the player's sprite when running
                    else:
                        self.animationController("run", last_held_direction, frame, superFrame)
                    self.HorizontalVelocity(self.last_held_direction, self.skidding, playerSprite)
            else:
                self.HorizontalVelocity(self.last_held_direction, self.skidding, playerSprite)
            # Change Sprite to ducking sprite if down is held
            if keys[self.down]:
                self.animationController("duck", last_held_direction, frame, superFrame)

        # Set the last held direction to left, and update the player's walk animation if they're on the ground           
        elif keys[self.left]:
            self.last_held_direction = "left"
            # Check to see if the player is on the ground before applying the sprite change
            if (self.check_jump(cmap) == True):
                # Check to see if ducking
                if keys[self.down]:
                    self.animationController("duck", last_held_direction, frame, superFrame)
                    self.Friction()
                else:
                    # Update the player's sprite when walking
                    if (self.x_velocity >= -2):
                        self.animationController("walk", last_held_direction, frame, superFrame)
                    # Update the player's sprite when running
                    else:
                        self.animationController("run", last_held_direction, frame, superFrame)
                    self.HorizontalVelocity(self.last_held_direction, self.skidding, playerSprite)
            else:
                self.HorizontalVelocity(self.last_held_direction, self.skidding, playerSprite)                
            # Change Sprite to ducking sprite if down is held
            if keys[self.down]:
                self.animationController("duck", last_held_direction, frame, superFrame)

        elif keys[self.down]:
            # If the player is on the ground, make them duck
            if self.check_jump(cmap) == True:
                self.animationController("duck", last_held_direction, frame, superFrame)
            # Apply friction to the player
            self.Friction()
                
        # Apply friction to the player if they are not holding a button or ducking
        # (slow them to a hault)
        else:
            # Apply friction to the player
            self.Friction()

        # Check to see if the player can jump
        if keys[self.up]:
            if self.check_jump(cmap) == True and self.released_up == True:
                # Update the player's sprite, then apply vertical velocity
                self.animationController("jump", last_held_direction, frame, superFrame)
                self.VerticalVelocity()
                playSound(jump)
                self.released_up = False
                if keys[self.down]:
                    self.animationController("duck", last_held_direction, frame, superFrame)

            else:
                # Update the player's sprite if the peak of the jump has been passed, then apply gravity
                if (self.y_velocity > 0):
                    self.animationController("fall", last_held_direction, frame, superFrame)
                self.gravity(GRAVITY,level,cmap)
                if keys[self.down]:
                    self.animationController("duck", last_held_direction, frame, superFrame)
            


        # Apply gravity to the player
        elif (self.check_jump(cmap) == False):
            # Update the player's sprite if the peak of the jump has been passed, then apply gravity
            if (self.y_velocity > 0):
                self.animationController("fall", last_held_direction, frame, superFrame)
            self.gravity(GRAVITY,level,cmap)
            self.released_up = True
            if keys[self.down]:
                self.animationController("duck", last_held_direction, frame, superFrame)

        else:
            if keys[self.down]:
                self.animationController("down", last_held_direction, frame, superFrame)
            self.gravity(GRAVITY,level,cmap)
            self.released_up = True
        self.y = round(self.y)

    # Print stats of the player when called
    def __str__(self):
        return "Player X Velocity: {}\nPlayer Y Velocity: {}\nPlayer X: {}\nPlayer Y: {}"\
            .format(self.x_velocity, self.y_velocity, self.x, self.y)
