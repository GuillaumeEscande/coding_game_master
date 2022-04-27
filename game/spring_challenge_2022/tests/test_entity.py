import unittest
import numpy

from entity import *


def test_monster(capsys):
    monster = Monster(1, numpy.array([1, 2]), 10, True, 11, numpy.array([3, 4]), True, False)
    assert monster.id == 1
    assert numpy.array_equal(monster.pos, numpy.array([1, 2]))
    assert monster.shield == 10
    assert monster.is_controlled == True
    assert monster.health == 11
    assert numpy.array_equal(monster.traj, numpy.array([3, 4]))
    assert monster.near_base == True
    assert monster.threat_for == False

def test_hero(capsys):
    hero = Hero(1, numpy.array([1, 2]), 10, True)
    assert hero.id == 1
    assert numpy.array_equal(hero.pos, numpy.array([1, 2]))
    assert hero.shield == 10
    assert hero.is_controlled == True
