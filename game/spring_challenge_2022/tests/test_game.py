from unittest.mock import MagicMock

from game import *


def test_game():
    
    my_hero = MagicMock()
    enemy_hero = MagicMock()

    monster = MagicMock()
    
    me = MagicMock()
    enemy = MagicMock()

    game = Game(me, enemy)

    assert game.me == me
    assert game.enemy == enemy


    game.add_monster(monster)
    assert len(game.monsters) == 1
    assert game.monsters[0] == monster

    
    game.add_hero(my_hero, True)
    game.add_hero(enemy_hero, False)

    assert len(game.my_heros) == 1
    assert game.my_heros[0] == my_hero
    assert len(game.enemy_heros) == 1
    assert game.enemy_heros[0] == enemy_hero



