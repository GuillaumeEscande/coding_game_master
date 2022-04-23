from cglogger import CGLogger

class GLogger(CGLogger):

    @classmethod
    def wait(cls, comment=""):
        cls.print("WAIT %s"%(comment))

    @classmethod
    def move(cls, pos, comment=""):
        cls.print("MOVE %d %d %s"%(pos[0], pos[1], comment))

    @classmethod
    def spell(cls, spell, pos, comment=""):
        cls.print("SPELL %s %d %d %s"%(spell, pos[0], pos[1], comment))