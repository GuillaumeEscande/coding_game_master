
from __future__ import annotations
from dataclasses import dataclass
import math 

@dataclass
class Board:
    width: int
    height: int
    neighbors_id: List[List[int]]

    def get_distance(self, case_from, case_to):
        return math.sqrt( math.pow(case_from.x - case_to.x, 2) + math.pow(case_from.y - case_to.y, 2) )
    
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