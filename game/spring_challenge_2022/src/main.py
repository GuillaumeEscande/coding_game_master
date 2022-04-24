import math
import numpy

from glogger import GLogger

from entity import *
from game import *
from init import *
from strategy import *

initializer = Initializer()

board = initializer.read_board()

heroes_per_player = int(input())  # Always 3

while True:
    me = initializer.read_player()
    enemy = initializer.read_player()
    game = initializer.read_game()

    strategy = Strategy(board, game)
    
    strategy.play_defensive(game.my_heros[0], board.pos_def_2_1)
    strategy.play_defensive(game.my_heros[1], board.pos_def_2_2)

    strategy.play_ultra_defensive(game.my_heros[2], board.pos_center_ultradef)