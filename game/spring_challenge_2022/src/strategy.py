import numpy

class Strategy() :
    def __init__(self, board, game):
        self.__game = game
        self.__board = board
        self.__nearest_monster = self.__game.get_nearest_monsters(self.__board.my_base)


    def play_defensive(self, hero, default_pos):
        
        
        if len(self.__nearest_monster):
            monster = self.__nearest_monster[0]

            dir_monster_base = monster.pos - self.__board.my_base
            dir_monster_base_normv = dir_monster_base/numpy.linalg.norm(dir_monster_base)
            step = dir_monster_base_normv * Hero.attack_range() * 0.9

            point_hero = monster.pos - step

            GLogger.move(point_hero)
        else:
            GLogger.move(default_pos)
