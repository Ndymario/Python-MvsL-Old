########################################################################
#   Author: Nolan Y. / bbomb64 / Christopher D.                        #
#                                                                      #
#   Description: Level/Tile handeler                                   #
########################################################################

#Add the path to the tile images folder
import os
from cmap import *
from raylibpy import load_texture

dirname = os.path.dirname(__file__)

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
    self.file.read(8) # do nothing with magic
    
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
        # Allows for many tile types, if you want to add more, follow the formula

        if tile["id"] == 1:
            tile_image = load_texture(dirname + "/Tiles/Grass_0.png")
        elif tile["id"] == 2:
            tile_image = load_texture(dirname + "/Tiles/Grass_1.png")
        elif tile["id"] == 3:
            tile_image = load_texture(dirname + "/Tiles/Grass_2.png")
        elif tile["id"] == 4:
            tile_image = load_texture(dirname + "/Tiles/Grass_3.png")
        elif tile["id"] == 5:
            tile_image = load_texture(dirname + "/Tiles/Grass_4.png")
        elif tile["id"] == 6:
            tile_image = load_texture(dirname + "/Tiles/Grass_5.png")
        elif tile["id"] == 7:
            tile_image = load_texture(dirname + "/Tiles/Grass_6.png")
        elif tile["id"] == 8:
            tile_image = load_texture(dirname + "/Tiles/Grass_7.png")
        elif tile["id"] == 9:
            tile_image = load_texture(dirname + "/Tiles/Grass_8.png")
        elif tile["id"] == 10:
            tile_image = load_texture(dirname + "/Tiles/Grass_9.png")
        elif tile["id"] == 11:
            tile_image = load_texture(dirname + "/Tiles/Grass_10.png")
        elif tile["id"] == 12:
            tile_image = load_texture(dirname + "/Tiles/Grass_11.png")
        elif tile["id"] == 13:
            tile_image = load_texture(dirname + "/Tiles/Grass_12.png")
        elif tile["id"] == 14:
            tile_image = load_texture(dirname + "/Tiles/Pipe_1.png")
        elif tile["id"] == 15:
            tile_image = load_texture(dirname + "/Tiles/Pipe_2.png")
        elif tile["id"] == 16:
            tile_image = load_texture(dirname + "/Tiles/Pipe_3.png")
        elif tile["id"] == 17:
            tile_image = load_texture(dirname + "/Tiles/Pipe_4.png")
        elif tile["id"] == 18:
            tile_image = load_texture(dirname + "/Tiles/Stone.png")
        elif tile["id"] == 19:
            tile_image = load_texture(dirname + "/Tiles/barrier.png")

      if not at_end:
        self.tiles.append(Tile(tile_image,1, tile["x"] * 16, tile["y"] * 16, tile["width"] * 16, tile["height"] * 16))

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
