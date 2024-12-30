from board import Cell

class Action(object):

    def print(self):
        pass

    def execute(self):
        CGLogger.print(self.str())

    
    @classmethod
    def execute_all(cls, actions: list[Action]):
        CGLogger.print(';'.join([a.str() for a in actions]))

class Wait(Action):

    def execute(self):
        GLogger.wait()

class Message(Action):
    __message: str

    def __init__(self, message):
        self.__message = message

    @property
    def message(self) -> str:
        return self.__message

    def str(self):
        return "MESSAGE %s"%(self.__message)

class Beacon(Action):
    __cell: Cell
    __strength: int

    def __init__(self, cell: Cell, strength: int):
        Action.__init__(self)
        self.__cell = cell
        self.__strength = strength

    @property
    def cell(self):
        return self.__cell

    def str(self):
        return "BEACON %d %d"%(self.__cell.index, self.__strength)

class Line(Action):
    __cell1: Cell
    __cell2: Cell
    __strength: int

    def __init__(self, cell1: Cell, cell2: Cell, strength: int):
        Action.__init__(self)
        self.__cell1 = cell1
        self.__cell2 = cell2
        self.__strength = strength

    @property
    def cell(self):
        return self.__cell

    def str(self):
        return "LINE %d %d %d"%(self.__cell1.index, self.__cell2.index, self.__strength)