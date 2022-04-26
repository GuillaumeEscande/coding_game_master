import numpy

from actions import *

monster_to_ignore=set()



class Tactic() :
    def __init__(self, board, game):
        self.__game = game
        self.__board = board


    def play_defensive(self, hero, default_pos):
        
        threat_monters = self.__game.threat_monsters
        nearest_threat_monster = self.__board.get_nearest_monsters(self.__board.my_base, threat_monters)
        
        nearest_threat_monster = [m for m in nearest_threat_monster if m.id not in monster_to_ignore]
        
        potential_threat_monsters = self.__game.potential_threat_monsters
        nearest_potential_threat_monsters = self.__board.get_nearest_monsters(self.__board.my_base, potential_threat_monsters)
        
        nearest_potential_threat_monsters = [m for m in nearest_potential_threat_monsters if m.id not in monster_to_ignore]
        
        if len(nearest_threat_monster):
            monster = nearest_threat_monster[0]
            point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
            return Move(point_hero)
        elif len(nearest_potential_threat_monsters):
            monster = potential_threat_monsters[0]
            point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
            return Move(point_hero)
        else:
            nearest_monsters = self.__board.get_nearest_monsters(hero.pos, self.__game.monsters)
            if len(nearest_monsters):
                monster = nearest_monsters[0]
                if self.__board.get_distance_of(self.__board.my_base, monster.pos) < 10000 :
                    point_hero = self.__board.better_defensive_pos(hero, default_pos, monster)
                    return Move(point_hero)
                else:
                    return Move(default_pos)
            else:
                return Move(default_pos)




    def play_ultra_defensive(self, hero, default_pos, monster_rank=0):
        
        threat_monters = self.__game.threat_monsters
        nearest_threat_monster = self.__board.get_nearest_monsters(self.__board.my_base, threat_monters)
        
        if len(nearest_threat_monster):
            monster = nearest_threat_monster[monster_rank]
            # Get distance of base
            base_distance = self.__board.get_distance_of(self.__board.my_base, monster.pos)
            if base_distance < 2000 and self.__game.me.mana > Action.SPELL_MANA:
                return Wind(self.__board.my_ennemy_base)
            else :
                point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
                return Move(point_hero)
        else:
            return Move(default_pos)



    def play_offensive_control(self, hero, default_pos):
        
        potential_threat_monsters = self.__game.potential_threat_monsters

        potential_threat_monsters = [m for m in potential_threat_monsters if m.id not in monster_to_ignore]
        
        if len(potential_threat_monsters):

            # On change le monstre le plus proche de la base potentielement daneureux
            nearest_potential_threat_monsters = self.__board.get_nearest_monsters(self.__board.my_base, list(potential_threat_monsters))

            GLogger.debug( [str(m.id) for m in nearest_potential_threat_monsters] )
            
            monster = nearest_potential_threat_monsters[0]
            if self.__board.get_distance_of(hero.pos, monster.pos) < Control.RANGE and self.__game.me.mana > Action.SPELL_MANA * 2:
                GLogger.spell_control(monster.id, self.__board.my_ennemy_base)
                monster_to_ignore.add(monster.id)
            else :
                point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
                return Move(point_hero)
        
        else:
            # On envoie le monstre le plus proche vers l'ennemy
            nearest_monsters = self.__board.get_nearest_monsters(hero.pos, self.__game.monsters)
            nearest_monsters = [m for m in nearest_monsters if m.id not in monster_to_ignore]

            
            if len(nearest_monsters):
                monster = nearest_monsters[0]
                
                if self.__game.me.mana > 50 and self.__board.get_distance_of(hero.pos, monster.pos) < Control.RANGE and self.__game.me.mana > Action.SPELL_MANA * 2:
                    monster_to_ignore.add(monster.id)
                    return Control(monster.id, self.__board.my_ennemy_base)
                else :
                    point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
                    return Move(point_hero)
            else :
                return Move(default_pos + numpy.random.randint(1000, size=(2)))
        
            


    def play_ultra_offensive_shield(self, hero, default_pos):

        nearest_monsters = self.__board.get_nearest_monsters(self.__board.my_ennemy_base, self.__game.monsters)
        nearest_monsters = [m for m in nearest_monsters if not m.shield > 1]

        if len(nearest_monsters) :
            monster = nearest_monsters[0]
            if self.__board.get_distance_of(self.__board.my_ennemy_base, monster.pos) < 4000 :
                if self.__board.get_distance_of(hero.pos, monster.pos) < Shield.RANGE and self.__game.me.mana > Action.SPELL_MANA * 2 and self.__board.get_distance_of(hero.pos, monster.pos) > Shield.RANGE :
                    GLogger.spell_shield(monster.id)
                else :
                    GLogger.move(monster.pos)
            else:
                GLogger.move(default_pos)
        else:
            GLogger.move(default_pos)