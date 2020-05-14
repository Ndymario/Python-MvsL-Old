########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #
#                                                                      #
#   Description: Level/Tile handeler                                   #
########################################################################

#Add the path to the tile images folder
import sys
sys.path.insert(1, "./Tiles")

class Tile(object):
    def __init__(self, tile_image, tile_friction, x, y, width = 16, height = 16):
        self.tile_image = tile_image
        self.tile_friction = tile_friction
        self.x = x
        self.y = y
        self.top = y - height
        self.width = width
        self.height = height
        self.left = x
        self.right = x + width

    def __str__(self):
        return "Tile X Coord: {}\nTile Y Coord: {}".format(self.x, self.y)

class Level():
  def __init__(self, fn):
    self.fn = fn
    self.file = None
    self.bg_id = None
    self.tiles = []
    self.sprites = []

    self.open_file()
    self.read_bg()
    self.read_tiles()
    self.read_sprites()

  def open_file(self):
    self.file = open(self.fn, "rb")

    file_magic = self.file.read(4)
    if file_magic != b'PLVL':
      print("File is not a valid level file!")
      exit(1)

  def read_bg(self):
    self.bg_id = int.from_bytes(self.file.read(2), byteorder='big')

  def read_tiles(self):
    self.file.read(4) # do nothing with magic
    
    # read all tiles in chunk
    at_end = False
    while not at_end:

      tile = {
        "id": None,
        "x": None,
        "y": None,
        "width": None,
        "height": None,
      }

      for i in range(5):
        short = self.file.read(2)
        if short == b'\xff\xff':
          at_end = True
          break
        tile[list(tile)[i]] = int.from_bytes(short,  byteorder='big')
      if not at_end:
        self.tiles.append(Tile("Tiles/Grass_Top.png",1, tile["x"] * 16, tile["y"] * 16, tile["width"] * 16, tile["height"] * 16))

  def read_sprites(self):
    self.file.read(4) # do nothing with magic

    # read all sprites in chunk
    at_end = False
    while not at_end:

      sprite = {
          "id": None,
          "x": None,
          "y": None,
      }
      
      for i in range(3):
        short = self.file.read(2)
        if short == b'\xff\xff':
          at_end = True
          break
        sprite[list(sprite)[i]] = int.from_bytes(short,  byteorder='big')
      if not at_end:
        self.sprites.append(sprite)

  def in_tile(self,x,y):
      for tile in self.tiles:
          if tile.top < y and tile.y >= y and tile.left - 20 < x and x < tile.right:
                return self.nearest_surface(x,y,tile)
      return False

  def under_tile(self, x, y):
      for tile in self.tiles:
          if tile.y == y and x + 20 > tile.left and x < tile.right:
              return tile.y
      return False
    
  def tile_on(self,x,y):
      for tile in self.tiles:
          if (y  == tile.top) and x > tile.left - 20 and x < tile.right:
                return tile.top
      return False

  def nearest_surface(self,x,y,tile):
      if y == tile.y:
          if 20 + x - tile.left > tile.right - x:
              return False,tile.right
          else:
              return False,tile.left - 20
      if y-tile.top > tile.y-y:
          if 20 + x - tile.left > tile.right - x:
              if tile.right - x > tile.y - y:
                  return True,tile.y
              else:
                  return False,tile.right
          else:
              if 20+x-tile.left > tile.y-y:
                  return True,tile.y
              else:
                  return False,tile.left - 20
          return tile.y
      else:
          if 20 + x - tile.left > tile.right - x:
              if tile.right - x > y-tile.top:
                  return True,tile.top
              else:
                  return False,tile.right
          else:
              if 20 + x-tile.left > y-tile.top:
                  return True,tile.top
              else:
                  return False,tile.left - 20

