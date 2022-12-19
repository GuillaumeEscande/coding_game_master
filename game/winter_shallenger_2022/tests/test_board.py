import unittest
import numpy
import os
import sys

from init import *
from board import BoardParam


    
def test_init_neighbors_id():
    neighbors_id = BoardParam.get_neighbors_id(14, 7)
    assert neighbors_id[0] == [14, 1]
    assert neighbors_id[1] == [15, 0, 2]
    assert neighbors_id[16] == [2, 30, 15, 17]


def test_get_recycling_value(resource_path_root):
    initializer = Initializer()
    sys.stdin = open(os.path.join(resource_path_root, "test_board", "board.txt"), "r", encoding="utf-8")
    board_param = initializer.read_board_param()
    board = initializer.read_board(board_param)

    assert board.get_recycling_value(board.tiles[0]) == 9
    assert board.get_recycling_value(board.tiles[45]) == 27
    
def test_get_neighbors(resource_path_root):
    initializer = Initializer()
    sys.stdin = open(os.path.join(resource_path_root, "test_board", "board.txt"), "r", encoding="utf-8")
    board_param = initializer.read_board_param()
    board = initializer.read_board(board_param)

    assert len(board.get_neighbors( board.tiles[16] )) == 3

    
def test_get_real_distance(resource_path_root):
    initializer = Initializer()
    sys.stdin = open(os.path.join(resource_path_root, "test_board", "board.txt"), "r", encoding="utf-8")
    board_param = initializer.read_board_param()
    board = initializer.read_board(board_param)

    assert board.get_real_distance( board.tiles[14], board.tiles[0] ) == 9999
    assert board.get_real_distance( board.tiles[0], board.tiles[1] ) == 9999
    assert board.get_real_distance( board.tiles[4], board.tiles[6] ) == 5

    
def test_get_fly_distance(resource_path_root):
    initializer = Initializer()
    sys.stdin = open(os.path.join(resource_path_root, "test_board", "board.txt"), "r", encoding="utf-8")
    board_param = initializer.read_board_param()
    board = initializer.read_board(board_param)

    assert board.get_fly_distance( board.tiles[14], board.tiles[0] ) == 1.0
    assert board.get_fly_distance( board.tiles[0], board.tiles[1] ) == 1.0
    assert board.get_fly_distance( board.tiles[4], board.tiles[6] ) == 4.0