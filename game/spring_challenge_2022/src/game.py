import numpy 

class Board() :
    def __init__(self, my_base):
        self.__my_base = my_base

    @property
    def my_base(self):
        return self.__my_base

    @property
    def is_top_left(self):
        return numpy.array_equal(self.__my_base, Board.top_left())

    @classmethod
    def size(cls):
        return numpy.array([17630, 9000])

    @classmethod
    def center(cls):
        return cls.size() / 2

    @classmethod
    def top_left(cls):
        return numpy.array([0, 0])

    @classmethod
    def bottom_right(cls):
        return cls.size()

    @property
    def pos_def_1(self):
        if self.is_top_left :
            return numpy.array([3300, 2600])
        else:
            return numpy.array([14550, 5800])

    @property
    def pos_def_2(self):
        if self.is_top_left :
            return numpy.array([4500, 6400])
        else:
            return numpy.array([13130, 2600])

    @property
    def pos_def_3(self):
        if self.is_top_left :
            return numpy.array([9500, 2331])
        else:
            return numpy.array([8130, 6669])



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

    def get_nearest_monsters(self, pos):
        tmp_list = self.monsters
        tmp_list.sort(key=lambda m: numpy.linalg.norm(m.pos-pos))
        return tmp_list