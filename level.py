########################################################################
#   Author: Nolan Y.                                                   #
#                                                                      #
#   Description: Level/Tile handeler                                   #
########################################################################

#Add the path to the tile images folder
import sys
sys.path.insert(1, "./Tiles")

class Tile(object):
    def __init__(self, tile_image, tile_friction, x, y, height = 16, width = 16):
        self.tile_image = tile_image
        self.tile_friction = tile_friction
        self.x = x
        self.y = y
        self.top = y - height
        self.left = x - (width/2)
        self.right = x + (width/2)

    def __str__(self):
        return "Tile X Coord: {}\nTile Y Coord: {}".format(self.x, self.y)

tile = Tile("Tiles/Grass_Top.png", 0.0, 100,  150)