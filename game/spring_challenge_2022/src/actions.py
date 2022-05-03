import numpy
from board import Board
from glogger import GLogger

class Action():
    SPELL_MANA = 10
    ATTACK_RANGE = 800
    ATTACK_HIT = 2

    def __init__(self):
        self._comment = None

    @property
    def comment(self):
        return self._comment

    def set_comment(self, comment):
        self._comment = comment

    def execute(self):
        pass

    def equals(self):
        False
    

class Wait(Action):

    def __init__(self):
        Action.__init__(self)

    def execute(self):
        GLogger.wait(self._comment)

class Move(Action):

    RANGE = 800

    def __init__(self, pos):
        Action.__init__(self)
        self.__pos = Board.crop_position(pos)

    @property
    def pos(self):
        return self.__pos

    def execute(self):
        GLogger.move(self.__pos, self._comment)

class Wind(Action):

    RANGE = 1280

    def __init__(self, target):
        Action.__init__(self)
        self.__target = Board.crop_position(target)

    @property
    def target(self):
        return self.__target

    def execute(self):
        GLogger.spell_wind(self.__target, self._comment)

class Shield(Action):

    RANGE = 2200

    def __init__(self, id):
        Action.__init__(self)
        self.__id = id

    @property
    def id(self):
        return self.__id

    def execute(self):
        GLogger.spell_shield(self.__id, self._comment)

class Control(Action):

    RANGE = 2200

    def __init__(self, id, target):
        Action.__init__(self)
        self.__id = id
        self.__target = Board.crop_position(target)

    @property
    def id(self):
        return self.__id

    @property
    def target(self):
        return self.__target

    def execute(self):
        GLogger.spell_control(self.__id, self.__target, self._comment)

