import numpy

from monster_finder import *
from entity import Monster

import pytest

@pytest.fixture
def monster_list():
    monster_list = list()
    monster_list.append(Monster(1, numpy.array([0, 10]), 0, True, 11, numpy.array([0, 0]), 1, 1))
    monster_list.append(Monster(2, numpy.array([0, 20]), 0, False, 1, numpy.array([0, 0]), 1, 2))
    monster_list.append(Monster(3, numpy.array([0, 30]), 10, True, 5, numpy.array([0, 0]), 0, 0))
    monster_list.append(Monster(4, numpy.array([0, 40]), 0, True, 6, numpy.array([0, 0]), 0, 1))
    monster_list.append(Monster(5, numpy.array([10, 10]), 0, False, 3, numpy.array([0, 0]), 0, 2))
    monster_list.append(Monster(6, numpy.array([100, 10]), 4, True, 5, numpy.array([0, 0]), 0, 0))
    monster_list.append(Monster(7, numpy.array([100, 20]), 7, False, 14, numpy.array([0, 0]), 0, 0))
    monster_list.append(Monster(8, numpy.array([100, 30]), 1, False, 9, numpy.array([0, 0]), 0, 0))
    monster_list.append(Monster(9, numpy.array([100, 40]), 9, False, 1, numpy.array([0, 0]), 0, 0))
    return monster_list

def test_find_getter_setter(monster_list):
    monster_finder = MonsterFinder(monster_list)
    assert monster_finder.monsters == monster_list

def test_find_distance(monster_list):
    monster_finder = MonsterFinder(monster_list)
    
    result = monster_finder.find_distance(numpy.array([10, 10]), distance_min=15 ).monsters
    assert len(result) == 6
    assert result[0].id == 3
    assert result[1].id == 4
    assert result[2].id == 6
    assert result[3].id == 7
    assert result[4].id == 8
    assert result[5].id == 9

    result = monster_finder.find_distance(numpy.array([10, 10]), distance_max=30  ).monsters
    assert len(result) == 4
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[2].id == 3
    assert result[3].id == 5

    result = monster_finder.find_distance(numpy.array([10, 10]), distance_min=15, distance_max=30  ).monsters
    assert len(result) == 1
    assert result[0].id == 3



def test_find_threat(monster_list):
    monster_finder = MonsterFinder(monster_list)

    result = monster_finder.find_threat(threat_for = True ).monsters
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 4
    
    result = monster_finder.find_threat(threat_for = False ).monsters
    assert len(result) == 2
    assert result[0].id == 2
    assert result[1].id == 5
    
    result = monster_finder.find_threat(threat_for = None).monsters
    assert len(result) == 5
    assert result[0].id == 3
    assert result[1].id == 6
    assert result[2].id == 7
    assert result[3].id == 8
    assert result[4].id == 9


def test_find_target(monster_list):
    monster_finder = MonsterFinder(monster_list)

    result = monster_finder.find_target(target = True ).monsters
    assert len(result) == 1
    assert result[0].id == 1
    
    result = monster_finder.find_target(target = False ).monsters
    assert len(result) == 1
    assert result[0].id == 2
    
    result = monster_finder.find_target(target = None ).monsters
    assert len(result) == 7
    assert result[0].id == 3
    assert result[1].id == 4
    assert result[2].id == 5
    assert result[3].id == 6
    assert result[4].id == 7
    assert result[5].id == 8
    assert result[6].id == 9

def test_find_health(monster_list):
    monster_finder = MonsterFinder(monster_list)
    result = monster_finder.find_health(health_min = 5 ).monsters
    assert len(result) == 6
    assert result[0].id == 1
    assert result[1].id == 3
    assert result[2].id == 4
    assert result[3].id == 6
    assert result[4].id == 7
    assert result[5].id == 8
    
    result = monster_finder.find_health(health_max = 2 ).monsters
    assert len(result) == 2
    assert result[0].id == 2
    assert result[1].id == 9
    
    result = monster_finder.find_health(health_min = 6, health_max = 8 ).monsters
    assert len(result) == 1
    assert result[0].id == 4

def test_find_shield(monster_list):
    monster_finder = MonsterFinder(monster_list)
    result = monster_finder.find_shield(shield_min = 5 ).monsters
    assert len(result) == 3
    assert result[0].id == 3
    assert result[1].id == 7
    assert result[2].id == 9
    
    result = monster_finder.find_shield(shield_max = 2 ).monsters
    assert len(result) == 5
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[2].id == 4
    assert result[3].id == 5
    assert result[4].id == 8
    
    result = monster_finder.find_shield(shield_min = 6, shield_max = 8 ).monsters
    assert len(result) == 1
    assert result[0].id == 7


def test_find_controlled(monster_list):
    monster_finder = MonsterFinder(monster_list)
    result = monster_finder.find_controlled(True).monsters
    assert len(result) == 4
    assert result[0].id == 1
    assert result[1].id == 3
    assert result[2].id == 4
    assert result[3].id == 6

    result = monster_finder.find_controlled(False).monsters
    assert len(result) == 5
    assert result[0].id == 2
    assert result[1].id == 5
    assert result[2].id == 7
    assert result[3].id == 8
    assert result[4].id == 9


def test_filter_by_id(monster_list):
    monster_finder = MonsterFinder(monster_list)

    ignore_list = [1, 2, 6, 7, 8, 4]

    result = monster_finder.filter_by_id(ids=ignore_list ).monsters
    assert len(result) == 3
    assert result[0].id == 3
    assert result[1].id == 5
    assert result[2].id == 9

def test_order_by_distance(monster_list):
    monster_finder = MonsterFinder(monster_list)

    result = monster_finder.order_by_distance(numpy.array([10, 10]) ).monsters
    assert len(result) == 9
    assert result[0].id == 5
    assert result[1].id == 1
    assert result[2].id == 2
    assert result[3].id == 3
    assert result[4].id == 4
    assert result[5].id == 6
    assert result[6].id == 7
    assert result[7].id == 8
    assert result[8].id == 9

    result = monster_finder.order_by_distance(numpy.array([10, 10]), True ).monsters
    assert len(result) == 9
    assert result[0].id == 9
    assert result[1].id == 8
    assert result[2].id == 7
    assert result[3].id == 6
    assert result[4].id == 4
    assert result[5].id == 3
    assert result[6].id == 2
    assert result[7].id == 1
    assert result[8].id == 5

def test_order_by_health(monster_list):
    monster_finder = MonsterFinder(monster_list)

    result = monster_finder.order_by_health().monsters
    assert len(result) == 9
    assert result[0].id == 2
    assert result[1].id == 9
    assert result[2].id == 5
    assert result[3].id == 3
    assert result[4].id == 6
    assert result[5].id == 4
    assert result[6].id == 8
    assert result[7].id == 1
    assert result[8].id == 7

    result = monster_finder.order_by_health(reverse=True).monsters
    assert len(result) == 9
    assert result[0].id == 7
    assert result[1].id == 1
    assert result[2].id == 8
    assert result[3].id == 4
    assert result[4].id == 3
    assert result[5].id == 6
    assert result[6].id == 5
    assert result[7].id == 2
    assert result[8].id == 9

def test_order_by_shield(monster_list):
    monster_finder = MonsterFinder(monster_list)

    result = monster_finder.order_by_shield().monsters
    assert len(result) == 9
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[2].id == 4
    assert result[3].id == 5
    assert result[4].id == 8
    assert result[5].id == 6
    assert result[6].id == 7
    assert result[7].id == 9
    assert result[8].id == 3

    result = monster_finder.order_by_shield(True).monsters
    assert len(result) == 9
    assert result[0].id == 3
    assert result[1].id == 9
    assert result[2].id == 7
    assert result[3].id == 6
    assert result[4].id == 8
    assert result[5].id == 1
    assert result[6].id == 2
    assert result[7].id == 4
    assert result[8].id == 5

def test_order_by_ratio_health_distance(monster_list):
    monster_finder = MonsterFinder(monster_list)

    result = monster_finder.order_by_ratio_health_distance(numpy.array([0, 0]), ).monsters
    assert len(result) == 9
    assert result[0].id == 9
    assert result[1].id == 6
    assert result[2].id == 2
    assert result[3].id == 8
    assert result[4].id == 7
    assert result[5].id == 4
    assert result[6].id == 3
    assert result[7].id == 5
    assert result[8].id == 1




#    monster_list.append(Monster(9, numpy.array([100, 40]), 9, False, 0, numpy.array([0, 0]), 0, 0))
#    monster_list.append(Monster(6, numpy.array([100, 10]), 4, True, 5, numpy.array([0, 0]), 0, 0))
#    monster_list.append(Monster(2, numpy.array([0, 20]), 0, False, 1, numpy.array([0, 0]), 1, 2))
#    monster_list.append(Monster(8, numpy.array([100, 30]), 1, False, 9, numpy.array([0, 0]), 0, 0))
#    monster_list.append(Monster(7, numpy.array([100, 20]), 7, False, 14, numpy.array([0, 0]), 0, 0))
#    monster_list.append(Monster(4, numpy.array([0, 40]), 0, True, 6, numpy.array([0, 0]), 0, 1))
#    monster_list.append(Monster(3, numpy.array([0, 30]), 10, True, 5, numpy.array([0, 0]), 0, 0))
#    monster_list.append(Monster(5, numpy.array([10, 10]), 0, False, 3, numpy.array([0, 0]), 0, 2))
#    monster_list.append(Monster(1, numpy.array([0, 10]), 0, True, 11, numpy.array([0, 0]), 1, 1))

