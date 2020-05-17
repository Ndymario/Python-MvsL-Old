########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D. / SkilLP               #                                                                      #
#   Description: My goal is to recreate the New Super Mario Bros.      #
#                DS gamemode Mario vs Luigi. Even if it's not perfect, #
#                it'll be a fun challenge!                             #
########################################################################

# Thanks to SkilLP, we now have a collision map, much more
# efficient when compared to how collision was done before
class CMap():
    def __init__(self, file = "1-1.cmap", width = 30, height = 20):
        self.file = file
        self.width = width
        self.height = height

    # It just works
    def get_tile(self, x, y, scale=16):
        buffer = open(self.file, "rb").read()
        return int(buffer[(int(x) // scale) + (int(y) // scale) * self.width])

    # Detects if a player is in a tile and puts the player
    # on the nearest open surface
    def in_tile(self,x,y,xv,yv):
          if self.get_tile(x, y) == 1:
              return self.nearest_surface(x,y,xv,yv)
          if self.get_tile(x+20, y) == 1:
              updated_position = self.nearest_surface(x+20,y,xv,yv)
              updated_position[0] += -20
              return updated_position
          if self.get_tile(x+20, y-22) == 1:
              updated_position = self.nearest_surface(x+20,y-22,xv,yv)
              updated_position[0] += -20
              updated_position[1] += 22
              return updated_position
          if self.get_tile(x, y-22) == 1:
              updated_position = self.nearest_surface(x,y-22,xv,yv)
              updated_position[1] += 22
              return updated_position
          return [x,y,xv,yv,False]

    # Finds the closest surface to player
    def nearest_surface(self,x,y,xv,yv):
          for i in range(32):
              if self.get_tile(x, y+i) == 0:
                  return [x,y+i,xv,0,True]

              if self.get_tile(x, y-i) == 0:
                  return [x,y-i,xv,0,True]
                
              if self.get_tile(x-i, y) == 0:
                  return [x-i,y,0,yv,True]
                
              if self.get_tile(x+i, y) == 0:
                  return [x+i,y,0,yv,True]
          return [x,y,xv,yv,False]

    # Looks at collision map and checks if player is on a tile
    def on_tile(self,x,y):
        if self.get_tile(x,y) == 0 and self.get_tile(x,y+1) == 1:
            return True,y
        if self.get_tile(x+20,y) == 0 and self.get_tile(x+20,y+1) == 1:
            return True,y
        return False
