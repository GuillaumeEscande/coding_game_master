import numpy

from board import *
from game import *

class Initializer():
    def __init__(self):
        pass

    def read_board_param(self):
        #Init Board
        width, height = [int(i) for i in input().split()]
        neighbors_id = BoardParam.get_neighbors_id(width, height)

        return BoardParam(width, height, neighbors_id)

    def read_matter(self):
        #Init Board
        my_matter, opp_matter = [int(j) for j in input().split()]
        return my_matter, opp_matter

    def read_board(self, board_param):
        tiles = []
        my_units = []
        my_recyclers = []
        my_tiles = []
        my_empty = []
        opp_units = []
        opp_recyclers = []
        opp_tiles = []
        opp_empty = []
        neutral_tiles = []

        for y in range(board_param.height):
            for x in range(board_param.width):
                # owner: 1 = me, 0 = foe, -1 = neutral
                # recycler, can_build, can_spawn, in_range_of_recycler: 1 = True, 0 = False
                scrap_amount, owner, units, recycler, can_build, can_spawn, in_range_of_recycler = [int(k) for k in input().split()]
                id = y*board_param.width + x
                tile = Tile(id, x, y, scrap_amount, owner, units, recycler == 1, can_build == 1, can_spawn == 1, in_range_of_recycler == 1)

                tiles.append(tile)

                if tile.owner == ME:
                    my_tiles.append(tile)
                    if tile.units > 0:
                        my_units.append(tile)
                    elif tile.recycler:
                        my_recyclers.append(tile)
                    else :
                        my_empty.append(tile)
                elif tile.owner == OPP:
                    opp_tiles.append(tile)
                    if tile.units > 0:
                        opp_units.append(tile)
                    elif tile.recycler:
                        opp_recyclers.append(tile)
                    else :
                        opp_empty.append(tile)
                else:
                    neutral_tiles.append(tile)

        return Board(board_param, tiles, my_units, my_recyclers, my_tiles, my_empty, opp_units, opp_recyclers, opp_tiles, opp_empty, neutral_tiles)