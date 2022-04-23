import math
import numpy as np

from glogger import GLogger

class Board() :
    def __init__(self, my_base, size=np.array([17630, 9000]) ):
        self.__size = size
        self.__my_base = my_base

    @property
    def my_base(self):
        return self.__my_base
        
    @property
    def center(self):
        return self.__size / 2


class Player() :
    def __init__(self, health, mana):
        self.__health = health
        self.__mana = mana

    @property
    def health(self):
        return self.__health
        
    @property
    def mana(self):
        return self.__mana


class Entity() :
    def __init__(self, id, pos, shield, is_controlled):
        self.__id = id
        self.__pos = pos
        self.__shield = shield
        self.__is_controlled = is_controlled
        
    @property
    def id(self):
        return self.__id
        
    @property
    def pos(self):
        return self.__pos
        
    @property
    def shield(self):
        return self.__shield
        
    @property
    def is_controlled(self):
        return self.__is_controlled


class Monster(Entity) :
    def __init__(self, id, pos, shield, is_controlled, health, traj, near_base, threat_for):
        Entity.__init__(self, id, pos, shield, is_controlled)
        self.__health = health
        self.__traj = traj
        self.__near_base = near_base
        self.__threat_for = threat_for

    @property
    def health(self):
        return self.__health
        
    @property
    def traj(self):
        return self.__traj
        
    @property
    def near_base(self):
        return self.__near_base
        
    @property
    def threat_for(self):
        return self.__threat_for


class Hero(Entity) :
    def __init__(self, id, pos, shield, is_controlled):
        Entity.__init__(self, id, pos, shield, is_controlled)

class Game() :
    def __init__(self):
        self.__monsters = list()
        self.__my_heros = list()
        self.__enemy_heros = list()

    @property
    def monsters(self):
        return self.__monsters

    def add_monster(self, monster):
        self.__monsters.append(monster)
        
    @property
    def my_heros(self):
        return self.__my_heros
        
    @property
    def enemy_heros(self):
        return self.__enemy_heros

    def add_hero(self, hero, mine):
        if mine :
            self.__my_heros.append(hero)
        else:
            self.__enemy_heros.append(hero)


class Initializer():
    def __init__(self):
        pass

    def read_board(self):
        #Init Board
        base_x, base_y = [int(i) for i in input().split()]
        base=np.array([base_x, base_y])
        return Board( base )

    def read_player(self):
        #Init Board
        health, mana = [int(j) for j in input().split()]
        return Player(health, mana)

    def read_game(self):
        game = Game()
        entity_count = int(input())  # Amount of heros and monsters you can see
        for i in range(entity_count):
            _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]

            if _type == 0 :
                monster = Monster(int(_id), np.array([x, y]), int(shield_life), bool(is_controlled), int(health), np.array([vx, vy]), bool(near_base), bool(threat_for))
                game.add_monster(monster)
            elif _type == 1 :
                hero = Hero(int(_id), np.array([x, y]), int(shield_life), bool(is_controlled))
                game.add_hero(hero, True)
            elif _type == 1 :
                hero = Hero(int(_id), np.array([x, y]), int(shield_life), bool(is_controlled))
                game.add_hero(hero, True)

        return game



initializer = Initializer()

board = initializer.read_board()

GLogger.debug(board)

heroes_per_player = int(input())  # Always 3

while True:
    me = initializer.read_player()
    enemy = initializer.read_player()

    game = initializer.read_game()

    for i in range(heroes_per_player):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        hero = game.my_heros[i]
        monsters = game.monsters

        
        monsters.sort(key=lambda m: np.linalg.norm(m.pos-board.my_base))

        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
        if len(monsters):
            if i > 0:
                GLogger.move( monsters[0].pos )
            else :
                if len(monsters) > 1:
                    GLogger.move( monsters[1].pos )
                else :
                    if np.array_equal(board.my_base, np.array((0, 0))):
                        GLogger.move(np.array([3300, 2600]))
                    else :
                        GLogger.move(np.array([15630, 7000]))

        else:
            if np.array_equal(board.my_base, np.array((0, 0))):
                if i == 0 :
                    print("MOVE 3300 2600")
                elif i == 1 :
                    print("MOVE 4500 6400")
                elif i == 2 :
                    print("MOVE 9500 2331")
            else :
                if i == 0 :
                    print("MOVE 14550 5800")
                elif i == 1 :
                    print("MOVE 13130 2600")
                elif i == 2 :
                    print("MOVE 8130 6669")
