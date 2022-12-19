import math
import numpy
import random
from datetime import datetime

from actions import *
from game import *
from init import *

from cglogger import CGLogger


initializer = Initializer()

board_param = initializer.read_board_param()

while True:

    start = datetime.now()
    my_matter, opp_matter = initializer.read_matter()
    board = initializer.read_board(board_param)

    CGLogger.debug("Init time = ", str((datetime.now() - start).total_seconds() * 1000))
    start = datetime.now()
    
    actions = []

    my_empty_cases = board.my_empty

    # Build
    if my_matter > 10 and len(board.my_recyclers) < len(board.opp_recyclers):
        
        target_recycler_value = 0
        target = None
        for target_choice in my_empty_cases:
            recycler_value = board.get_recycling_value(target_choice)
            if recycler_value > target_recycler_value and target_choice.can_build :
                target = target_choice
                target_recycler_value = recycler_value

        if False and target:
            my_empty_cases.remove(target)
            actions.append(Build(target.x, target.y))
            my_matter -= 10

    
    CGLogger.debug("Build time = ", str((datetime.now() - start).total_seconds() * 1000))

    # Spawn
    # Todo spawn on border or detect isolated cases
    while my_matter > 10 and len(my_empty_cases) > 2 :
        spawn_case = random.choice(my_empty_cases)
        if spawn_case.can_spawn:
            my_empty_cases.remove(spawn_case)
            actions.append(Spawn(1, spawn_case.x, spawn_case.y))
            my_matter -= 10

    target_cases = []

    
    CGLogger.debug("Spawn time = ", str((datetime.now() - start).total_seconds() * 1000))

    #Move
    for unit in board.my_units:
        move_start = datetime.now()
        targets = []
        for target in board.opp_tiles:
            if target not in target_cases:
                distance = board.get_fly_distance(unit, target)
                if len(targets) < 5 or distance < board.param.width/2:
                    targets.append( (target, distance) )

        
        #CGLogger.debug("Move select time = ", str((datetime.now() - move_start).total_seconds() * 1000))

        targets.sort(key=lambda x: x[1])
        
        #CGLogger.debug("Move sort select time = ", str((datetime.now() - move_start).total_seconds() * 1000))

        while len(targets) and board.get_real_distance(unit, targets[0][0]) == 9999 :
            targets.pop(0)
        
        #CGLogger.debug("Move scheck faisability time = ", str((datetime.now() - move_start).total_seconds() * 1000))

        if len(targets) :
            target = targets[0][0]
            actions.append(Move(unit.units, unit.x, unit.y, target.x, target.y))
            my_empty_cases.append(unit)
            target_cases.append(target)

        if (datetime.now() - start).total_seconds() * 1000 > 40:
            break
        
        #CGLogger.debug("Move end time = ", str((datetime.now() - move_start).total_seconds() * 1000))

    CGLogger.debug("Move time = ", str((datetime.now() - start).total_seconds() * 1000))



    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    CGLogger.print(';'.join(map(str, actions)) if len(actions) > 0 else 'WAIT')