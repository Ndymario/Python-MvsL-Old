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
        self.width = width
        self.left = x - (width/2)
        self.right = x + (width/2)

    def __str__(self):
        return "Tile X Coord: {}\nTile Y Coord: {}".format(self.x, self.y)

levelchunk1 = [Tile("Tiles/Grass_Top.png", 0.0, 85,  150),Tile("Tiles/Grass_Top.png", 0.0, 115,  150), Tile("Tiles/Grass_Top.png", 0.0, 130,  150), Tile("Tiles/Grass_Top.png", 0.0, 145,  150), Tile("Tiles/Grass_Top.png", 0.0, 160,  150), Tile("Tiles/Grass_Top.png", 0.0, 100,  150), Tile("Tiles/Grass_Top.png", 0.0, 70,  150), Tile("Tiles/Grass_Top.png", 0.0, 115,  135)]
tile = Tile("Tiles/Grass_Top.png", 0.0, 100,  150)
