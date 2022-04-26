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

    tactic = Tactic(board, game)
    
    #tactic.play_defensive(game.my_heros[0], board.pos_center_def)

    if me.health > 2 :

        tactic.play_ultra_offensive_shield(game.my_heros[0], board.pos_ultra_attack).execute()
        
        tactic.play_offensive_control(game.my_heros[1], board.pos_center_offensive).execute()

        tactic.play_ultra_defensive(game.my_heros[2], board.pos_center_ultradef).execute()
        
    else:

        tactic.play_ultra_offensive_shield(game.my_heros[0], board.pos_ultra_attack).execute()
        
        tactic.play_defensive(game.my_heros[1], board.pos_center_ultradef).execute()

        tactic.play_ultra_defensive(game.my_heros[2], board.pos_center_ultradef).execute()