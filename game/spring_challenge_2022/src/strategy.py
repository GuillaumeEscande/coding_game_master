import numpy

class Strategy() :
    def __init__(self, board, game):
        self.__game = game
        self.__board = board


    def play_defensive(self, hero, default_pos):
        
        threat_monters = self.__game.threat_monsters
        nearest_threat_monster = self.__board.get_nearest_monsters(hero.pos, threat_monters)
        
        potential_threat_monsters = self.__game.potential_threat_monsters
        nearest_potential_threat_monsters = self.__board.get_nearest_monsters(hero.pos, potential_threat_monsters)
        
        if len(nearest_threat_monster):
            monster = nearest_threat_monster[0]
            point_hero = self.__board.better_defensive_attack(hero, self.__board.my_base, monster)
            GLogger.move(point_hero)
        elif len(nearest_potential_threat_monsters):
            monster = potential_threat_monsters[0]
            point_hero = self.__board.better_defensive_attack(hero, self.__board.my_base, monster)
            GLogger.move(point_hero)
        else:
            GLogger.move(default_pos)




    def play_ultra_defensive(self, hero, default_pos):
        
        threat_monters = self.__game.threat_monsters
        nearest_threat_monster = self.__board.get_nearest_monsters(self.__board.my_base, threat_monters)
        
        if len(nearest_threat_monster):
            monster = nearest_threat_monster[0]
            # Get distance of base
            base_distance = self.__board.get_distance_of(self.__board.my_base, monster.pos)
            if base_distance < 2000:
                GLogger.spell_control(monster.id, self.__board.ennemy_base)
            else :
                point_hero = self.__board.better_defensive_attack(hero, self.__board.my_base, monster)
                GLogger.move(point_hero)
        else:
            GLogger.move(default_pos)
