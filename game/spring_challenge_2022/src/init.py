import numpy

from board import Board
from game import Player, Game
from entity import Hero, Monster

class Initializer():
    def __init__(self):
        pass

    def read_board(self):
        #Init Board
        base_x, base_y = [int(i) for i in input().split()]
        base=numpy.array([base_x, base_y])
        return Board( base )

    def read_player(self):
        #Init Board
        health, mana = [int(j) for j in input().split()]
        return Player(health, mana)

    def read_game(self, me, ennemy):
        game = Game(me, ennemy)
        entity_count = int(input())  # Amount of heros and monsters you can see
        for i in range(entity_count):
            _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]

            if _type == 0 :
                monster = Monster(int(_id), numpy.array([x, y]), int(shield_life), bool(is_controlled), int(health), numpy.array([vx, vy]), bool(near_base), bool(threat_for))
                game.add_monster(monster)
            elif _type == 1 :
                hero = Hero(int(_id), numpy.array([x, y]), int(shield_life), bool(is_controlled))
                game.add_hero(hero, True)
            elif _type == 2 :
                hero = Hero(int(_id), numpy.array([x, y]), int(shield_life), bool(is_controlled))
                game.add_hero(hero, False)

        return game