import unittest
import numpy

from board import Board


    
def test_init_neighbors_id():
    neighbors_id = Board.get_neighbors_id(14, 7)
    assert neighbors_id[0] == [14, 1]
    assert neighbors_id[1] == [15, 0, 2]
    assert neighbors_id[16] == [2, 30, 15, 17]