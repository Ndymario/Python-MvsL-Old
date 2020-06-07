########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D. / SkilLP               #                                                                      #
#   Description: File for the Collision Map Handler                    #
########################################################################

# Thanks to SkilLP, we now have a collision map, much more
# efficient when compared to how collision was done before

class CMap():
    def __init__(self, file = "Level/1-1.lvl"):
        self.file = file
        self.width = 0
        self.height = 0
        self.cmalp = []

    def create_cmap(self,lvl):
        CMap_data = []
        LVL_file = open(lvl, "rb").read()
        self.width = int.from_bytes(LVL_file[4:6], "big")
        self.height = int.from_bytes(LVL_file[6:8], "big")

        for i in range(self.width):
            for j in range(self.height):
                CMap_data.append(0)

        index = LVL_file.find(b'TILE') + 4

        while LVL_file[index:index + 2] != b'\xff\xff':
            index += 2
            t_x = int.from_bytes(LVL_file[index: index + 2], byteorder='big')
            index += 2
            t_y = int.from_bytes(LVL_file[index: index + 2], byteorder='big')
            index += 2
            t_width = int.from_bytes(LVL_file[index: index + 2], byteorder='big')
            index += 2
            t_height = int.from_bytes(LVL_file[index: index + 2], byteorder='big')
            index += 2
            for i in range(t_height):
                for j in range(t_width):
                    CMap_data[t_x + j + (t_y - i) * self.width] = 1
        for i in range(self.height):
            temp_map = CMap_data[0 + self.width*i:self.width+ self.width*i]
            self.cmalp.append(temp_map)

    def check_box(self,x,y,b,h):
        collisions = 0
        for o in range(round(int(y-h))//16,round(int(y))//16+1):
            temp_map = self.cmalp[o]
            if 1 in temp_map[round(x/16):round((x+b)/16)+1]:
                collisions = 1
        return collisions
            
    # Detects if a player is in a tile and puts the player
    # on the nearest open surface
    def in_tile(self,x,y,xv,yv,pw,ph):
          if self.check_box(x,y,pw,ph) == 1:
              return self.nearest_surface(x,y,xv,yv,pw,ph)
          return [x,y,xv,yv,False]

    # Finds the closest surface to player
    def nearest_surface(self,x,y,xv,yv,pw,ph):
          for i in range(16):
              if self.check_box(x,y-i,pw,ph) != 1:
                  if yv >= 0:
                      return [x,y-i,xv,0,True]
                  else:
                      return [x,y-i,xv,yv,True]

              if self.check_box(x,y+i,pw,ph) != 1:
                  if yv <= 0:
                      return [x,y+i,xv,0,True]
                  else:
                      return [x,y+i,xv,yv,True]
                
              if self.check_box(x-i,y,pw,ph) != 1:
                  if xv >= 0:
                      return [x-i,y,0,yv,True]
                  else:
                      return [x-i,y,xv,yv,True]
                
              if self.check_box(x+i,y,pw,ph) != 1:
                  if xv <= 0:
                      return [x+i,y,0,yv,True]
                  else:
                      return [x+i,y,xv,yv,True]

              if self.check_box(x+i,y-i,pw,ph) != 1:
                  return [x+i,y-i,0,0,True]
                
              if self.check_box(x-i,y-i,pw,ph) != 1:
                  return [x-i,y-i,0,0,True]
                
              if self.check_box(x+i,y+i,pw,ph) != 1:
                  return [x+i,y+i,xv,yv,True]
                
              if self.check_box(x-i,y+i,pw,ph) != 1:
                  return [x-i,y+i,xv,yv,True]
                
          return [x,y,xv,yv,False]

    # Looks at collision map and checks if player is on a tile
    def on_tile(self,x,y,pw,ph):
        if self.check_box(x,y,pw,ph) == 0 and self.check_box(x,y+1,pw,ph) == 1:
            return True,y
        return False
