import math
import numpy
import random

from actions import *
from game import *
from init import *

from cglogger import CGLogger


initializer = Initializer()

board = initializer.read_board()

while True:

    my_matter, opp_matter = initializer.read_matter()
    game = initializer.read_game(board)

    
    actions = []

    my_empty_cases = [x for x in game.my_tiles if x not in game.my_recyclers]
    my_empty_cases = [x for x in my_empty_cases if x not in game.my_units]

    # Build
    if my_matter > 10 and len(game.my_recyclers) < len(game.opp_recyclers):
        build_case = random.choice(my_empty_cases)
        my_empty_cases.remove(build_case)
        actions.append(Build(build_case.x, build_case.y))
        my_matter -= 10

    # Spawn
    while my_matter > 10 and len(my_empty_cases) > 2 :
        spawn_case = random.choice(my_empty_cases)
        my_empty_cases.remove(spawn_case)
        actions.append(Spawn(1, spawn_case.x, spawn_case.y))
        my_matter -= 10

    #Move
    for unit in game.my_units:
        target_distance = 9999
        target = None
        for target_choice in game.neutral_tiles:
            distance = board.get_distance(unit, target_choice)
            if distance < target_distance :
                target = target_choice
                target_distance = distance
        for target_choice in game.opp_tiles :
            distance = board.get_distance(unit, target_choice)
            if distance < target_distance :
                target = target_choice
                target_distance = distance
        if target :
            actions.append(Move(unit.units, unit.x, unit.y, target.x, target.y))
            my_empty_cases.append(unit)
            if target in my_empty_cases : my_empty_cases.remove(target)




    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(';'.join(map(str, actions)) if len(actions) > 0 else 'WAIT')