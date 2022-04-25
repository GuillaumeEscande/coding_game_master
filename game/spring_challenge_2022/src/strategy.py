import numpy

monster_to_ignore=set()

class Strategy() :
    def __init__(self, board, game):
        self.__game = game
        self.__board = board


    def play_defensive(self, hero, default_pos):
        
        threat_monters = self.__game.threat_monsters
        nearest_threat_monster = self.__board.get_nearest_monsters(self.__board.my_base, threat_monters)
        
        potential_threat_monsters = self.__game.potential_threat_monsters
        nearest_potential_threat_monsters = self.__board.get_nearest_monsters(self.__board.my_base, potential_threat_monsters)
        
        if len(nearest_threat_monster):
            monster = nearest_threat_monster[0]
            point_hero = self.__board.better_defensive_attack(hero, self.__board.my_base, monster)
            GLogger.move(point_hero)
        elif len(nearest_potential_threat_monsters):
            monster = potential_threat_monsters[0]
            point_hero = self.__board.better_defensive_attack(hero, self.__board.my_base, monster)
            GLogger.move(point_hero)
        else:
            nearest_monsters = self.__board.get_nearest_monsters(hero.pos, self.__game.monsters)
            if len(nearest_monsters):
                monster = nearest_monsters[0]
                if self.__board.get_distance_of(self.__board.my_base, monster.pos) < 10000 :
                    point_hero = self.__board.better_defensive_attack(hero, default_pos, monster)
                    GLogger.move(point_hero)
                else:
                    GLogger.move(default_pos)
            else:
                GLogger.move(default_pos)




    def play_ultra_defensive(self, hero, default_pos, monster_rank=0):
        
        threat_monters = self.__game.threat_monsters
        nearest_threat_monster = self.__board.get_nearest_monsters(self.__board.my_base, threat_monters)
        
        if len(nearest_threat_monster):
            monster = nearest_threat_monster[monster_rank]
            # Get distance of base
            base_distance = self.__board.get_distance_of(self.__board.my_base, monster.pos)
            if base_distance < 2000:
                #GLogger.spell_control(monster.id, self.__board.ennemy_base)
                GLogger.spell_wind(self.__board.ennemy_base)
            else :
                point_hero = self.__board.better_defensive_attack(hero, self.__board.my_base, monster)
                GLogger.move(point_hero)
        else:
            GLogger.move(default_pos)



    def play_offensive_control(self, hero, default_pos):
        
        potential_threat_monsters = self.__game.potential_threat_monsters
        
        GLogger.debug( [str(m.id) for m in potential_threat_monsters] )
        GLogger.debug( monster_to_ignore )

        potential_threat_monsters = list(set(monster_to_ignore).difference(set(potential_threat_monsters)))
        
        GLogger.debug( [str(m.id) for m in potential_threat_monsters] )
        
        if not len(potential_threat_monsters):
            GLogger.move(default_pos)
            return

        # On change le monstre le plus proche de la base potentielement daneureux
        nearest_potential_threat_monsters = self.__board.get_nearest_monsters(self.__board.my_base, list(potential_threat_monsters))

        GLogger.debug( [str(m.id) for m in nearest_potential_threat_monsters] )
        
        monster = nearest_potential_threat_monsters[0]
        if self.__board.get_distance_of(hero.pos, monster.pos) < CONST_CONTROL_RANGE :
            GLogger.spell_control(monster.id, self.__board.ennemy_base)
            monster_to_ignore.add(monster.id)
        else :
            point_hero = self.__board.better_defensive_attack(hero, self.__board.my_base, monster)
            GLogger.move(point_hero)
        
            