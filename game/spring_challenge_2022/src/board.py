import numpy 

from cglogger import CGLogger

class Board() :
    def __init__(self, my_base):
        self.__my_base = my_base
        if self.is_top_left :
            self.__base_dir = 1
        else :
            self.__base_dir = -1

        self.__pos_def_3_1 = self.get_pos_from_base((90/4)*1, 5000)
        self.__pos_def_3_2 = self.get_pos_from_base((90/4)*2, 5000)
        self.__pos_def_3_3 = self.get_pos_from_base((90/4)*3, 5000)
        
        self.__pos_def_2_1 = self.get_pos_from_base(30, 4000)
        self.__pos_def_2_2 = self.get_pos_from_base(60, 4000)
        self.__pos_center_def = self.get_pos_from_base(45, 6000)
        self.__pos_center_ultradef = self.get_pos_from_base(45, 2000)

    @property
    def my_base(self):
        return self.__my_base

    @property
    def ennemy_base(self):
        if self.is_top_left:
            return Board.bottom_right()
        else:
            return Board.top_left()

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
    def pos_def_3_1(self):
        return self.__pos_def_3_1

    @property
    def pos_def_3_2(self):
        return self.__pos_def_3_2

    @property
    def pos_def_3_3(self):
        return self.__pos_def_3_3

    @property
    def pos_def_2_1(self):
        return self.__pos_def_2_1

    @property
    def pos_def_2_2(self):
        return self.__pos_def_2_2

    @property
    def pos_center_def(self):
        return self.__pos_center_def

    @property
    def pos_center_ultradef(self):
        return self.__pos_center_ultradef
        

    def get_pos_from_base(self, angle_deg, distance):
        rot_vectom = numpy.array([numpy.cos(numpy.deg2rad(angle_deg)), numpy.sin(numpy.deg2rad(angle_deg))])
        if self.is_top_left:
            pos_f = self.__my_base + rot_vectom * distance
        else :
            pos_f = self.__my_base - rot_vectom[::-1] * distance

        return pos_f.astype(int)
        
    
    def get_nearest_monsters(self, pos, monters):
        tmp_list = monters
        tmp_list.sort(key=lambda m: numpy.linalg.norm(m.pos-pos))
        return tmp_list

    def get_distance_of(self, origin, target):
        distance_vect = origin - target

        GLogger.debug("origin", origin)
        GLogger.debug("target", target)
        GLogger.debug("distance_vect", distance_vect)
        GLogger.debug("get_distance_of", numpy.linalg.norm(distance_vect))

        return numpy.linalg.norm(distance_vect)

    def better_defensive_attack(self, hero, base, monster):
        dir_monster_base = monster.pos - base
        dir_monster_base_normv = dir_monster_base/numpy.linalg.norm(dir_monster_base)
        step = dir_monster_base_normv * Hero.attack_range() * 0.9

        point_hero = monster.pos - step
        return point_hero