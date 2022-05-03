import math
import numpy

from glogger import GLogger

from entity import *
from game import *
from init import *
from tactic import *
from monster_memory import *




initializer = Initializer()

board = initializer.read_board()

heroes_per_player = int(input())  # Always 3

monster_memory = MonsterMemory()

cmp = 0

while True:

    me = initializer.read_player()
    enemy = initializer.read_player()
    game = initializer.read_game(me, enemy)

    monster_memory.update(game.monsters, game.my_heros)
    monster_finder = MonsterFinder(monster_memory.monsters)


    tactic = Tactic(board, game, monster_finder)
    # 0 = defence
    tactic.new_protect_base(game.my_heros[0], board.pos_def_2_1).execute()
    # 1 = defence
    tactic.new_protect_base(game.my_heros[1], board.pos_def_2_2).execute()
    # 2 = defence
    tactic.new_protect_base(game.my_heros[2], board.pos_center_ultradef).execute()

    



    monster_memory.play_turn()