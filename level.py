########################################################################
#   Author: Nolan Y.                                                   #
#                                                                      #
#   Description: Level/Tile handeler                                   #
########################################################################

#Add the path to the tile images folder
import sys
sys.path.insert(1, "./Tiles")

class Tile(object):
    def __init__(self, tile_image, tile_friction, x, y):
        self.tile_image = tile_image
        self.tile_friction = tile_friction
        self.x = x
        self.y = y

    def __str__(self):
        return "Tile X Coord: {}\nTile Y Coord: {}".format(self.x, self.y)

