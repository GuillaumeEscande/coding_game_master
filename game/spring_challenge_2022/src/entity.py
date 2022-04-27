
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
    ATTACK_RANGE = 800
    def __init__(self, id, pos, shield, is_controlled):
        Entity.__init__(self, id, pos, shield, is_controlled)