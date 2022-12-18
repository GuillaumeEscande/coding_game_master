import numpy
from dataclasses import dataclass


COST_BUILD = 10
COST_SPAWN = 10

@dataclass
class Spawn:
    amount: int
    x: int
    y: int

    def __str__(action):
        return 'SPAWN {} {} {}'.format(action.amount, action.x, action.y)

@dataclass
class Move:
    amount: int
    from_x: int
    from_y: int
    to_x: int
    to_y: int
    
    def __str__(action):
        return 'MOVE {} {} {} {} {}'.format(action.amount, action.from_x, action.from_y, action.to_x, action.to_y)

@dataclass
class Build:
    x: int
    y: int
    
    def __str__(action):
        return 'BUILD {} {}'.format(action.x, action.y)
