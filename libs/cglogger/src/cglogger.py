import sys

class CGLogger():
    @classmethod
    def print(cls, *objects):
        print(*objects)

    @classmethod
    def debug(cls, *objects):
        print(*objects, file=sys.stderr)