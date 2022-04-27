from cglogger import CGLogger

class GLogger(CGLogger):

    @classmethod
    def wait(cls, comment=None):
        if not comment :
            comment=""
        cls.print("WAIT %s"%(comment))

    @classmethod
    def move(cls, pos, comment=None):
        if not comment :
            comment=""
        cls.print("MOVE %d %d %s"%(pos[0], pos[1], comment))

    @classmethod
    def spell_wind(cls, pos, comment=None):
        if not comment :
            comment=""
        cls.print("SPELL WIND %d %d %s"%(pos[0], pos[1], comment))

    @classmethod
    def spell_shield(cls, id, comment=None):
        if not comment :
            comment=""
        cls.print("SPELL SHIELD %d %s"%(id, comment))

    @classmethod
    def spell_control(cls, id, pos, comment=None):
        if not comment :
            comment=""
        cls.print("SPELL CONTROL %d %d %d %s"%(id, pos[0], pos[1], comment))