import numpy
from Board import Board

class Action():
    SPELL_MANA = 10
    def __init__(self):
        self._comment = None

    @property
    def comment(self):
        return self._comment

    def set_comment(self, comment):
        self._comment = comment

    def execute(self):
        pass

class Wait(Action):

    def __init__(self):
        pass

    def execute(self):
        GLogger.wait()

class Move(Action):

    def __init__(self, pos):
        
        pos[0] = max(pos[0], 0)
        pos[0] = min(pos[0], Board.SIZE[0])
        pos[1] = max(pos[1], 0)
        pos[1] = min(pos[1], Board.SIZE[1])
        
        self.__pos = pos

    def execute(self):
        GLogger.move(self.__pos)

class Wind(Action):

    RANGE = 1280

    def __init__(self, pos):

        pos[0] = max(pos[0], 0)
        pos[0] = min(pos[0], Board.SIZE[0])
        pos[1] = max(pos[1], 0)
        pos[1] = min(pos[1], Board.SIZE[1])

        self.__pos = pos

    def execute(self):
        GLogger.spell_wind(self.__pos)

class Shield(Action):

    RANGE = 2200

    def __init__(self, id):
        self.__id = id

    def execute(self):
        GLogger.spell_shield(self.__id)

class Control(Action):

    RANGE = 2200

    def __init__(self, id, pos):
        self.__id = id
        
        pos[0] = max(pos[0], 0)
        pos[0] = min(pos[0], Board.SIZE[0])
        pos[1] = max(pos[1], 0)
        pos[1] = min(pos[1], Board.SIZE[1])

        self.__pos = pos

    def execute(self):
        GLogger.spell_control(self.__id, self.__pos)

