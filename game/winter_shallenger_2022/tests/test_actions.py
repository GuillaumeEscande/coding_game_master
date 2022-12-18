import unittest
import numpy

from actions import *


def test_move(capsys):
    action = Move(1, 2, 3, 4, 5)
    assert str(action) == "MOVE 1 2 3 4 5"

def test_spawn(capsys):
    action = Spawn(1, 2, 3)
    assert str(action) == "SPAWN 1 2 3"

def test_build(capsys):
    action = Build(1, 2)
    assert str(action) == "BUILD 1 2"