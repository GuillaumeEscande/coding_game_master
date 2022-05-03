from board import Board 


class Entity() :
    def __init__(self, id, pos, shield, is_controlled):
        self._id = id
        self._pos = pos
        self._shield = shield
        self._is_controlled = is_controlled
        
    @property
    def id(self):
        return self._id
        
    @property
    def pos(self):
        return self._pos
        
    @property
    def shield(self):
        return self._shield
        
    @property
    def is_controlled(self):
        return self._is_controlled


class Monster(Entity) :
    RANGE_MOVE=400
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
        
    def move_turn(self):
        self._pos += self.__traj

    def time_to_reach(self, posHeros):
        PosMon = self.pos
        for i in range(10):
            if Board.get_distance_of(posHeros, PosMon) < Action.ATTACK_RANGE + i * Move.RANGE:
                return i, PosMon
            PosMon = PosMon + self.traj
        return 1000, numpy.array([0,0])


class Hero(Entity) :
    ATTACK_RANGE = 800
    VISIBILITY = 2200 

    FactActionDef = 1
    FactActionExp = 1
    FactActionAtt = 1
    posRef = None
    type = 0 # 0 def , 1 milieu, 2 att

    def __init__(self, id, pos, shield, is_controlled):
        Entity.__init__(self, id, pos, shield, is_controlled)