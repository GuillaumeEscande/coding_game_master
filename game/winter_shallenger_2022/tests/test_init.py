import sys
import io
import os

from init import *


def test_read_board():
    initializer = Initializer()

    sys.stdin = io.StringIO('0 0')
    board = initializer.read_board()
    assert board.width == 0
    assert board.height == 0
    
    sys.stdin = io.StringIO('2 5')
    board = initializer.read_board()
    assert board.width == 2
    assert board.height == 5

def test_read_matter():
    initializer = Initializer()

    sys.stdin = io.StringIO('10 30')
    my_matter, opp_matter = initializer.read_matter()
    assert my_matter == 10
    assert opp_matter == 30

def test_read_game(resource_path):
    initializer = Initializer()
    
    sys.stdin = open(os.path.join(resource_path, "read_run.txt"), "r", encoding="utf-8")
    board = initializer.read_board()
    my_matter, opp_matter = initializer.read_matter()
    game = initializer.read_game(board)
    assert board.width == 14
    assert board.height == 7
    assert my_matter == 10
    assert opp_matter == 10
    assert game.tiles[5].x == 5
    assert game.tiles[5].y == 0
    assert game.tiles[5].scrap_amount == 0
