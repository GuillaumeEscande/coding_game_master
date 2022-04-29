import unittest
import numpy

from board import Board


def test_get_pos_from_base_tl():
    board = Board(Board.top_left())
    pos_1 = board.get_pos_from_base(90/4, 6000)
    assert numpy.array_equal(numpy.array([5543, 2296]), pos_1)

    board = Board(Board.bottom_right())
    pos_1 = board.get_pos_from_base(90/4, 6000)
    assert numpy.array_equal(numpy.array([15333,  3456]), pos_1)
    
def test_get_pos_0():
    board = Board(Board.top_left())
    pos_1 = board.get_pos_from_base(0, 6000)
    assert numpy.array_equal(numpy.array([6000, 0]), pos_1)
    
    board = Board(Board.bottom_right())
    pos_1 = board.get_pos_from_base(0, 6000)
    assert numpy.array_equal(numpy.array([17630,  3000]), pos_1)
    
def test_get_pos_90():
    board = Board(Board.top_left())
    pos_1 = board.get_pos_from_base(90, 6000)
    assert numpy.array_equal(numpy.array([0,  6000]), pos_1)
    
    board = Board(Board.bottom_right())
    pos_1 = board.get_pos_from_base(90, 6000)
    assert numpy.array_equal(numpy.array([11630,  9000]), pos_1)


def test_crop_position():
    assert numpy.array_equal(numpy.array([10,  20]), Board.crop_position(numpy.array([10,  20])))
    assert numpy.array_equal(numpy.array([0,  20]), Board.crop_position(numpy.array([-10,  20])))
    assert numpy.array_equal(numpy.array([10,  0]), Board.crop_position(numpy.array([10,  -20])))
    assert numpy.array_equal(numpy.array([0,  0]), Board.crop_position(numpy.array([-10,  -20])))

def test_get_distance_of():
    assert Board.get_distance_of(numpy.array([0,  0]), numpy.array([0,  1])) == 1
    assert Board.get_distance_of(numpy.array([0,  0]), numpy.array([1,  0])) == 1
    assert Board.get_distance_of(numpy.array([0,  0]), numpy.array([0,  -2])) == 2
    assert Board.get_distance_of(numpy.array([0,  0]), numpy.array([-2,  0])) == 2
    assert Board.get_distance_of(numpy.array([0,  0]), numpy.array([5,  5])) == 7.0710678118654755

def test_better_defensive_pos():
    pass

def test_real_pos():
    assert numpy.array_equal(Board.real_pos(numpy.array([0,  0]), numpy.array([100,  0]), 10), numpy.array([10,  0]))
    assert numpy.array_equal(Board.real_pos(numpy.array([0,  0]), numpy.array([0,  100]), 10), numpy.array([0,  10]))
    assert numpy.array_equal(Board.real_pos(numpy.array([0,  0]), numpy.array([10,  10]), 100), numpy.array([10,  10]))


