
from __future__ import annotations
from dataclasses import dataclass
from astar import *
import math 

@dataclass
class Tile:
    id: int
    x: int
    y: int
    scrap_amount: int
    owner: int
    units: int
    recycler: bool
    can_build: bool
    can_spawn: bool
    in_range_of_recycler: bool

@dataclass
class BoardParam:
    width: int
    height: int
    neighbors_id: List[List[int]]
    
    @classmethod
    def get_neighbors_id(self, width, height):
        neighbors_id = []
        for y in range(height):
            for x in range(width):
                case_eighbors_id = []
                if y > 0:
                    case_eighbors_id.append( (y-1) * width + x)
                if y < height - 1:
                    case_eighbors_id.append( (y+1) * width + x)
                if x > 0:
                    case_eighbors_id.append( y * width + x - 1)
                if x < width - 1:
                    case_eighbors_id.append( y * width + x + 1)

                neighbors_id.append(case_eighbors_id)

        return neighbors_id

@dataclass
class Board:
    param: BoardParam
    tiles: List[Tile]
    my_units: List[Tile]
    my_recyclers: List[Tile]
    my_tiles: List[Tile]
    my_empty: List[Tile]
    opp_units: List[Tile]
    opp_recyclers: List[Tile]
    opp_tiles: List[Tile]
    opp_empty: List[Tile]
    neutral_tiles: List[Tile]

    def get_fly_distance(self, case_from, case_to):
        return math.pow(case_from.x - case_to.x, 2) + math.pow(case_from.y - case_to.y, 2)
        
    def get_real_distance(self, case_from, case_to):
        path = astar(self, case_from, case_to)
        if path :
            return len(path)
        else :
            return 9999

    def get_recycling_value(self, case):
        value = case.scrap_amount
        for neighbor in self.get_neighbors(case):
            if not neighbor.in_range_of_recycler:
                value += neighbor.scrap_amount
        return value

    def get_neighbors(self, case):
        neighbors = []

        for case_id in self.param.neighbors_id[case.id]:
            tile = self.tiles[case_id]
            if tile.scrap_amount > 0 and not tile.recycler:
                neighbors.append(tile)

        return neighbors


    