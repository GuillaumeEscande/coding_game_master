import sys
import io
import os

from init import *


def test_read_board_param():
    initializer = Initializer()

    sys.stdin = io.StringIO('0 0')
    board_param = initializer.read_board_param()
    assert board_param.width == 0
    assert board_param.height == 0
    
    sys.stdin = io.StringIO('2 5')
    board_param = initializer.read_board_param()
    assert board_param.width == 2
    assert board_param.height == 5

def test_read_matter():
    initializer = Initializer()

    sys.stdin = io.StringIO('10 30')
    my_matter, opp_matter = initializer.read_matter()
    assert my_matter == 10
    assert opp_matter == 30

def test_read_board(resource_path):
    initializer = Initializer()
    
    sys.stdin = open(os.path.join(resource_path, "read_run.txt"), "r", encoding="utf-8")
    board_param = initializer.read_board_param()
    my_matter, opp_matter = initializer.read_matter()
    board = initializer.read_board(board_param)
    assert board_param.width == 14
    assert board_param.height == 7
    assert my_matter == 10
    assert opp_matter == 10
    assert board.tiles[5].x == 5
    assert board.tiles[5].y == 0
    assert board.tiles[5].scrap_amount == 0
