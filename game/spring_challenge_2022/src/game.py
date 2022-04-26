import numpy 
from enum import Enum

CONST_ATTACK_RANGE = 800 

CONST_WIND_RANGE = 1280
CONST_SHIELD_RANGE = 2200
CONST_CONTROL_RANGE = 2200

CONST_SPELL_MANA = 10

class Spell(Enum):
    WIND = "WIND"
    SHIELD = "SHIELD"
    CONTROL = "CONTROL"

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



class Game() :
    def __init__(self, me, ennemy):
        self.__monsters = list()
        self.__threat_monsters = list()
        self.__potential_threat_monsters = list()
        self.__no_threat_monsters = list()
        self.__my_heros = list()
        self.__enemy_heros = list()
        self.__me = me
        self.__ennemy = ennemy

    @property
    def me(self):
        return self.__me

    @property
    def ennemy(self):
        return self.__ennemy

    @property
    def monsters(self):
        return self.__monsters

    def add_monster(self, monster):
        self.__monsters.append(monster)
        if monster.threat_for == 1 :
            if monster.near_base == 1 :
                self.__threat_monsters.append(monster)
            else:
                self.__potential_threat_monsters.append(monster)
        else :
            self.__no_threat_monsters.append(monster)

    @property
    def threat_monsters(self):
        return self.__threat_monsters

    @property
    def potential_threat_monsters(self):
        return self.__potential_threat_monsters

    @property
    def no_threat_monsters(self):
        return self.__no_threat_monsters
        
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