from __future__ import annotations
from enum import Enum
from dataclasses import dataclass

from board import Board


ME = 1
OPP = 0
NONE = -1

@dataclass
class Game :
    board: Board