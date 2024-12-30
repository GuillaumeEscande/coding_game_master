import math
import numpy

from board import *
from actions import *
from cglogger import CGLogger

INF = float('inf')


board: Board = Board() 


CGLogger.debug("Nombre de celulles : %s"%board.number_of_cells)
CGLogger.debug("Totaux cristaux restant: %s"%board.total_cristal)


number_of_bases = int(input())
my_bases: list[int] = []
for i in input().split():
    my_base_index = int(i)
    my_bases.append(my_base_index)
opp_bases: list[int] = []
for i in input().split():
    opp_base_index = int(i)
    opp_bases.append(opp_base_index)



# game loop
while True:

    board.read_state()
    CGLogger.debug("Totaux cristaux restant: %s"%board.total_cristal)
    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>

    diamond :list[Cell] = [ cell for cell in board.cells if (cell.cell_type == 2 or cell.cell_type == 1) and cell.resources > 0]


    diamond.sort(key=lambda x: board.distances[my_base_index][x.index])

    CGLogger.debug("Diamond 1")
    for i in diamond:
        CGLogger.debug("Diamond %d %d"%(i.index, i.resources))

    needed_score = int(board.target_score * 1.1)

    computed_score = 0
    diamond_needed = []
    #diamond = list(filter(lambda x: (computed_score := computed_score + x.resources) <= needed_score, diamond))

    for cell in diamond:
        if cell.cell_type == 2 :
            computed_score += cell.resources
        diamond_needed.append(cell)
        if computed_score >= needed_score:
            break
    
    CGLogger.debug("Score needed : %d, score compute : %d"%(needed_score, computed_score))


    
    CGLogger.debug("Diamond 2")
    for i in diamond_needed:
        CGLogger.debug("Diamond %d %d"%(i.index, i.resources))

    actions = []
    
    for i in diamond_needed:
        cell1 = board.cells[my_base_index]
        cell2 = i
        distance = board.distances[cell1.index][cell2.index]
        actions.append(Line(cell1, cell2, distance))


    # TODO: choose actions to perform and push them into actions
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if len(actions) == 0:
        print('WAIT')
    else:
        Action().execute_all(actions)

