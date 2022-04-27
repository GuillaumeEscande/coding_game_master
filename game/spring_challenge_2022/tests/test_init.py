import sys
import io
import os

from init import *


def test_read_board():
    initializer = Initializer()

    sys.stdin = io.StringIO('0 0')
    board = initializer.read_board()
    assert board.is_top_left()
    
    sys.stdin = io.StringIO('17630 9000')
    board = initializer.read_board()
    assert board.is_bottom_right()

def test_read_player():
    initializer = Initializer()

    sys.stdin = io.StringIO('10 30')
    player = initializer.read_player()
    assert player.health == 10
    assert player.mana == 30

def test_read_game(resource_path):
    initializer = Initializer()

    sys.stdin = open(os.path.join(resource_path, "read_start.txt"), "r", encoding="utf-8")
    game = initializer.read_game(None, None)
    assert len(game.monsters) == 0
    assert len(game.my_heros) == 3
    assert len(game.enemy_heros) == 3

    
    sys.stdin = open(os.path.join(resource_path, "read_run.txt"), "r", encoding="utf-8")
    game = initializer.read_game(None, None)
    assert len(game.monsters) == 8
    assert len(game.my_heros) == 3
    assert len(game.enemy_heros) == 3
