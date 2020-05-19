########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D. / SkilLP               #                                                                      #
#   Description: File for the Collision Map Handler                    #
########################################################################

# Thanks to SkilLP, we now have a collision map, much more
# efficient when compared to how collision was done before
class CMap():
    def __init__(self, file = "1-1.cmap", width = 50, height = 20):
        self.file = file
        self.width = width
        self.height = height
        self.cmalp = []

    # It just works
    def get_tile(self, x, y, scale=16):
        buffer = open(self.file, "rb").read()
        return int(buffer[round(int(x) / scale) + round(int(y) / scale) * self.width])

    def check_box(self,x,y,b,h):
        collisions = 0
        for o in range(round(int(y-h)/16),round(int(y)/16)+1):
            temp_map = self.cmalp[o]
            if 1 in temp_map[round(x/16):round((x+b)/16)+1]:
                collisions = 1
        return collisions
            
    # Detects if a player is in a tile and puts the player
    # on the nearest open surface
    def in_tile(self,x,y,xv,yv):
          if self.check_box(x,y,20,20) == 1:
              return self.nearest_surface(x,y,xv,yv)
          return [x,y,xv,yv,False]

    # Finds the closest surface to player
    def nearest_surface(self,x,y,xv,yv):
          for i in range(16):
              if self.check_box(x,y+i,20,20) != 1:
                  return [x,y+i,xv,0,True]

              if self.check_box(x,y-i,20,20) != 1:
                  return [x,y-i,xv,0,True]
                
              if self.check_box(x-i,y,20,20) != 1:
                  return [x-i,y,0,yv,True]
                
              if self.check_box(x+i,y,20,20) != 1:
                  return [x+i,y,0,yv,True]

              if self.check_box(x+i,y+i,20,20) != 1:
                  return [x+i,y+i,0,0,True]
                
              if self.check_box(x-i,y+i,20,20) != 1:
                  return [x-i,y+i,0,0,True]
                
              if self.check_box(x+i,y-i,20,20) != 1:
                  return [x+i,y-i,0,0,True]
                
              if self.check_box(x-i,y-i,20,20) != 1:
                  return [x-i,y-i,0,0,True]
              
          return [x,y,xv,yv,False]

    # Looks at collision map and checks if player is on a tile
    def on_tile(self,x,y):
        if self.get_tile(x,y) == 0 and self.get_tile(x,y+1) == 1:
            return True,y
        if self.get_tile(x+20,y) == 0 and self.get_tile(x+20,y+1) == 1:
            return True,y
        return False
