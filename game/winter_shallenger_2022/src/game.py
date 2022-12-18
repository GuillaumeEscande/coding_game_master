from __future__ import annotations
from enum import Enum
from dataclasses import dataclass


ME = 1
OPP = 0
NONE = -1

@dataclass
class Tile:
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
class Game :
    tiles: List[Tile]
    my_units: List[Tile]
    opp_units: List[Tile]
    my_recyclers: List[Tile]
    opp_recyclers: List[Tile]
    opp_tiles: List[Tile]
    my_tiles: List[Tile]
    neutral_tiles: List[Tile]
