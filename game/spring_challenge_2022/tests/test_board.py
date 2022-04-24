import unittest
import numpy

from board import Board


def test_get_pos_from_base_tl(capsys):
    board = Board(Board.top_left())
    pos_1 = board.get_pos_from_base(90/4, 6000)
    assert numpy.array_equal(numpy.array([5543, 2296]), pos_1)

    board = Board(Board.bottom_right())
    pos_1 = board.get_pos_from_base(90/4, 6000)
    assert numpy.array_equal(numpy.array([15333,  3456]), pos_1)
    
def test_get_pos_0(capsys):
    board = Board(Board.top_left())
    pos_1 = board.get_pos_from_base(0, 6000)
    assert numpy.array_equal(numpy.array([6000, 0]), pos_1)
    
    board = Board(Board.bottom_right())
    pos_1 = board.get_pos_from_base(0, 6000)
    assert numpy.array_equal(numpy.array([17630,  3000]), pos_1)
    
def test_get_pos_90(capsys):
    board = Board(Board.top_left())
    pos_1 = board.get_pos_from_base(90, 6000)
    assert numpy.array_equal(numpy.array([0,  6000]), pos_1)
    
    board = Board(Board.bottom_right())
    pos_1 = board.get_pos_from_base(90, 6000)
    assert numpy.array_equal(numpy.array([11630,  9000]), pos_1)