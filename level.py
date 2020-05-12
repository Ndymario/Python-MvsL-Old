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

  def tile_on(self, x, y):
        for tile in self.tiles:
            if (y  >= tile.top) and y <= tile.top + 8 and x > tile.x - 18 and x < tile.x + tile.width:
                return tile
        return False
    
  def hit_under_tile(self, x, y,player):
        if player.y_velocity < 0:
            for tile in self.tiles:
                if (y > tile.y - 6) and y < tile.y and x > tile.x - 18 and x < tile.x + tile.width:
                    return tile
        return False

  def in_tile(self, x, y):
      for tile in self.tiles:
          if (y > tile.y - 8) and y <= tile.y - 1 and x < tile.width + tile.x and x >tile.x - 18:
              return tile
      return False

  def lr_tile_collision(self, x, y, v):
      for tile in self.tiles:
          if (y <= tile.top + tile.height) and y > tile.top and x > tile.x - 18 and x <= tile.x - 17:
              return tile.left - 18
          if (y <= tile.top + tile.height) and y > tile.top and x >= tile.x + tile.width - 1 and x < tile.x + tile.width:
              return tile.right
          if (y < tile.top + tile.height-4) and y > tile.top and x + v > tile.x - 18 and x + v <= tile.x - 7:
              return tile.left - 18
          if (y < tile.top + tile.height-4) and y > tile.top and x + v >= tile.x + tile.width - 10 and x + v < tile.x + tile.width:
              return tile.right
      return False

  def bottom_lr_tile_collision(self,x,y):
      for tile in self.tiles:
          if (y <= tile.top + tile.height) and y > tile.top and x > tile.x - 18 and x <= tile.x - 8:
                  return tile.left - 18
          if (y <= tile.top + tile.height) and y > tile.top and x >= tile.x + tile.width - 10 and x < tile.x + tile.width:
                  return tile.right
      return False
