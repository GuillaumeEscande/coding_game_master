import numpy
from board import Board
from glogger import GLogger

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
        Action.__init__(self)

    def execute(self):
        GLogger.wait(self._comment)

class Move(Action):

    def __init__(self, pos):
        Action.__init__(self)
        self.__pos = Board.crop_position(pos)

    def execute(self):
        GLogger.move(self.__pos, self._comment)

class Wind(Action):

    RANGE = 1280

    def __init__(self, pos):
        Action.__init__(self)
        self.__pos = Board.crop_position(pos)

    def execute(self):
        GLogger.spell_wind(self.__pos, self._comment)

class Shield(Action):

    RANGE = 2200

    def __init__(self, id):
        Action.__init__(self)
        self.__id = id

    def execute(self):
        GLogger.spell_shield(self.__id, self._comment)

class Control(Action):

    RANGE = 2200

    def __init__(self, id, pos):
        Action.__init__(self)
        self.__id = id
        self.__pos = Board.crop_position(pos)

    def execute(self):
        GLogger.spell_control(self.__id, self.__pos, self._comment)

