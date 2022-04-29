import math
import numpy

from glogger import GLogger

from entity import *
from game import *
from init import *
from tactic import *

initializer = Initializer()

board = initializer.read_board()

heroes_per_player = int(input())  # Always 3

while True:
    me = initializer.read_player()
    enemy = initializer.read_player()
    game = initializer.read_game(me, enemy)

    monster_finder = MonsterFinder(game.monsters)

    tactic = Tactic(board, game, monster_finder)

    tactic.new_protect_base(game.my_heros[0], board.pos_def_2_1).execute()
    
    tactic.new_protect_base(game.my_heros[1], board.pos_def_2_2).execute()

    tactic.new_protect_base(game.my_heros[2], board.pos_center_ultradef).execute()