import numpy 
from enum import Enum

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
    def __init__(self, me, enemy):
        self.__monsters = list()
        self.__my_heros = list()
        self.__enemy_heros = list()
        self.__me = me
        self.__enemy = enemy

    @property
    def me(self):
        return self.__me

    @property
    def enemy(self):
        return self.__enemy

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