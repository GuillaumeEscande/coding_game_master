import numpy 

from glogger import GLogger

class Board() :
    SIZE = numpy.array([17630, 9000])

    def __init__(self, my_base):
        self.__my_base = my_base
        if self.is_top_left(self.__my_base) :
            self.__base_dir = 1
        else :
            self.__base_dir = -1

        self.__pos_def_3_1 = self.get_pos_from_base((90/4)*1, 5000)
        self.__pos_def_3_2 = self.get_pos_from_base((90/4)*2, 5000)
        self.__pos_def_3_3 = self.get_pos_from_base((90/4)*3, 5000)
        
        self.__pos_def_2_1 = self.get_pos_from_base(30, 4000)
        self.__pos_def_2_2 = self.get_pos_from_base(60, 4000)
        self.__pos_center_def = self.get_pos_from_base(45, 6000)
        self.__pos_center_ultradef = self.get_pos_from_base(45, 3000)
        
        self.__pos_center_ultradef = self.get_pos_from_base(45, 2000)

        self.__pos_ultra_attack = self.get_pos_from_base(45, 4000, base=self.enemy_base(self.__my_base))

    @property
    def my_base(self):
        return self.__my_base

    def enemy_base(self, base=None):
        if self.is_top_left(base):
            return Board.bottom_right()
        else:
            return Board.top_left()
            
    @property
    def my_enemy_base(self):
        return self.enemy_base(base=self.__my_base)

    def is_top_left(self, base=None):
        if base is None :
            base = self.__my_base
        return numpy.array_equal(base, Board.top_left())

    def is_bottom_right(self, base=None):
        return not self.is_top_left(base)
    

    @classmethod
    def crop_position(cls, initial_pos):
        pos = initial_pos.copy()
        pos[0] = max(pos[0], 0)
        pos[0] = min(pos[0], Board.SIZE[0])
        pos[1] = max(pos[1], 0)
        pos[1] = min(pos[1], Board.SIZE[1])
        return pos

    @classmethod
    def size(cls):
        return Board.SIZE

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

    @property
    def pos_center_offensive(self):
        return self.center()

    @property
    def pos_ultra_attack(self):
        return self.__pos_ultra_attack
        

    def get_pos_from_base(self, angle_deg, distance, base=None):
        if base is None :
            base = self.__my_base
        rot_vectom = numpy.array([numpy.cos(numpy.deg2rad(angle_deg)), numpy.sin(numpy.deg2rad(angle_deg))])
        if self.is_top_left(base):
            pos_f = base + rot_vectom * distance
        else :
            pos_f = base - rot_vectom[::-1] * distance

        return pos_f.astype(int)
        
    
    @classmethod
    def get_nearest(cls, pos, entities):
        tmp_list = entities
        tmp_list.sort(key=lambda m: numpy.linalg.norm(m.pos-pos))
        return tmp_list

    @classmethod
    def get_distance_of(cls, origin, target):
        distance_vect = origin - target
        return numpy.linalg.norm(distance_vect)

    @classmethod
    def better_defensive_pos(cls, hero, base, monster):
        # TODO utiliser la diretion du monstre plusot que la position de la base
        dir_monster_base = monster.pos - base
        dir_monster_base_normv = dir_monster_base / numpy.linalg.norm(dir_monster_base)
        step = dir_monster_base_normv * Hero.ATTACK_RANGE * 0.9

        point_hero = monster.pos - step
        return point_hero

    @classmethod
    def real_pos(cls, inital_pos, target, max_range):
        real_target = target
        if Board.get_distance_of(inital_pos, target) > max_range :
            direction = target - inital_pos
            direction_normalized = direction / numpy.linalg.norm(direction)
            real_position = inital_pos + direction_normalized * max_range
            real_target = real_position.astype(int)
        
        return Board.crop_position(real_target)