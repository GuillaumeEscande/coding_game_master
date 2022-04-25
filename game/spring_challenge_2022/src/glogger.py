from cglogger import CGLogger

class GLogger(CGLogger):

    @classmethod
    def wait(cls, comment=""):
        cls.print("WAIT %s"%(comment))

    @classmethod
    def move(cls, pos, comment=""):
        x = pos[0]
        y = pos[1]
        if x < 0:
            x = 400
        if y < 0:
            y = 400
        cls.print("MOVE %d %d %s"%(x, y, comment))

    @classmethod
    def spell_wind(cls, pos, comment=""):
        cls.print("SPELL WIND %d %d %s"%(pos[0], pos[1], comment))

    @classmethod
    def spell_shield(cls, pos, comment=""):
        cls.print("SPELL SHIELD %d %d %s"%(pos[0], pos[1], comment))

    @classmethod
    def spell_control(cls, id, pos, comment=""):
        cls.print("SPELL CONTROL %d %d %d %s"%(id, pos[0], pos[1], comment))