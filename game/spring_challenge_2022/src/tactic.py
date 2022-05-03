import numpy

from actions import *
from action_checker import *

monster_to_ignore=set()



class Tactic() :
    HEALTH_DISTANCE_RATIO = 2/400
    def __init__(self, board, game, monster_finder):
        self.__game = game
        self.__board = board
        self.__monster_finder = monster_finder


    def __vital_protect(self, hero):
        # Trouver les monstres avec un rapport vie / distance impossible à kill
        vital_monster = self.__monster_finder.find_target(True).find_distance(self.__board.my_base, distance_max=10000).find_ratio_health_distance(self.__board.my_base, ratio_min=Tactic.HEALTH_DISTANCE_RATIO).order_by_ratio_health_distance(self.__board.my_base)
        
        # Trouver les monstres ataignables 
        if len(vital_monster.monsters) :
            act_check = ActionChecker(self.__game, vital_monster)

            wind = Wind(self.__board.my_enemy_base)
            result = act_check.check_action(wind, hero)

            if result.hit :
                wind.set_comment("vital_protect - wind")
                return wind

            control = Control(vital_monster.monsters[0].id, self.__board.my_enemy_base)
            result = act_check.check_action(control, hero)
            
            if result.hit :
                control.set_comment("vital_protect - control")
                return control

            return Move(vital_monster.monsters[0].pos)
        
        return None


    def __soft_defence(self, hero):
        # Trouver les mostres les plus proches de la base qui la target
        target_monsters = self.__monster_finder.find_target(True).find_distance(self.__board.my_base, distance_max=5000).order_by_distance(self.__board.my_base)
        
        if len(target_monsters.monsters) :
            act_check = ActionChecker(self.__game, target_monsters)

            move = Move(target_monsters.monsters[0].pos)
            result = act_check.check_action(move, hero)
            
            move.set_comment("soft_defence - move")
            return move
        
        return None

    def __preventive_defence(self, hero):
        # Trouver les mostres qui target la base
        target_monsters = self.__monster_finder.find_threat(True).find_distance(self.__board.my_base, distance_max=5000)
                
        if len(target_monsters.monsters) :
            act_check = ActionChecker(self.__game, target_monsters)

            move = Move(target_monsters.monsters[0].pos)
            result = act_check.check_action(move, hero)
            
            move.set_comment("preventive_defence - move")
            return move
    
    def new_protect_base(self, hero, default_pos, wind=True, control=True, close_distance=4000):
        vital = self.__vital_protect(hero)

        if vital:
            return vital
        
        soft = self.__soft_defence(hero)
        if soft:
            return soft
            
        preventive = self.__preventive_defence(hero)
        if preventive:
            return preventive

        
        move = Move(default_pos)
        move.set_comment("new_protect_base - default_pos")
        return move


    # def play_defensive(self, hero, default_pos):
        
    #     nearest_threat_monster = self.__monster_finder.find(near_pos=self.__board.my_base, threat_for=True, ignore_id=monster_to_ignore)
        
    #     nearest_potential_threat_monsters = self.__monster_finder.find(near_pos=self.__board.my_base, target=True, ignore_id=monster_to_ignore)
                
        
    #     if len(nearest_threat_monster.monsters):
    #         monster = nearest_threat_monster.monsters[0]
    #         point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
    #         return Move(point_hero)
    #     elif len(nearest_potential_threat_monsters.monsters):
    #         monster = potential_threat_monsters.monsters[0]
    #         point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
    #         return Move(point_hero)
    #     else:
    #         nearest_monsters = self.__monster_finder.monsters.find(near_pos=hero.pos, threat_for=False)
    #         if len(nearest_monsters.monsters):
    #             monster = nearest_monsters.monsters[0]
    #             return Move(nearest_monsters)
    #         else:
    #             return Move(default_pos)




    # def play_ultra_defensive(self, hero, default_pos, monster_rank=0):
        
    #     nearest_threat_monster = self.__monster_finder.find(near_pos=self.__board.my_base, threat_for=True)

        
    #     if len(nearest_threat_monster):

    #         nearest_threat_monster_range_wind = nearest_threat_monster.find(near_pos=self.__board.my_base, distance_pos=hero.pos, distance_max=Action.SPELL_MANA )

    #         if self.__monster_finder.me.mana > Action.SPELL_MANA and len(nearest_threat_monster_range_wind.monsters) > 0 :
    #             return Wind(self.__board.my_enemy_base)
    #         else :
    #             point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, nearest_threat_monster[0])
    #             return Move(point_hero)
    #     else:
    #         return Move(default_pos)



    # def play_offensive_control(self, hero, default_pos):

    #     nearest_potential_threat_monsters = self.__monster_finder.find(near_pos=self.__board.my_base, target=True, ignore_id=monster_to_ignore)
        
    #     if len(nearest_potential_threat_monsters.monsters):
            
    #         nearest_potential_threat_monsters = nearest_potential_threat_monsters.find(near_pos=self.__board.my_base, distance_max=2000 )
    #         monster = nearest_potential_threat_monsters[0]
    #         if self.__board.get_distance_of(hero.pos, monster.pos) < Control.RANGE and self.__game.me.mana > Action.SPELL_MANA * 2:
    #             GLogger.spell_control(monster.id, self.__board.my_enemy_base)
    #             monster_to_ignore.add(monster.id)
    #         else :
    #             point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
    #             return Move(point_hero)
        
    #     else:
    #         # On envoie le monstre le plus proche vers l'enemy
    #         nearest_monsters = self.__board.get_nearest(hero.pos, self.__monster_finder.monsters)
    #         nearest_monsters = [m for m in nearest_monsters if m.id not in monster_to_ignore]

            
    #         if len(nearest_monsters):
    #             monster = nearest_monsters[0]
                
    #             if self.__game.me.mana > 50 and self.__board.get_distance_of(hero.pos, monster.pos) < Control.RANGE and self.__game.me.mana > Action.SPELL_MANA * 2:
    #                 monster_to_ignore.add(monster.id)
    #                 return Control(monster.id, self.__board.my_enemy_base)
    #             else :
    #                 point_hero = self.__board.better_defensive_pos(hero, self.__board.my_base, monster)
    #                 return Move(point_hero)
    #         else :
    #             return Move(default_pos + numpy.random.randint(1000, size=(2)))
        
            


    # def play_ultra_offensive_shield(self, hero, default_pos):

    #     nearest_monsters = self.__board.get_nearest(self.__board.my_enemy_base, self.__monster_finder.monsters)
    #     nearest_monsters = [m for m in nearest_monsters if not m.shield > 1]

    #     if len(nearest_monsters) :
    #         monster = nearest_monsters[0]
    #         if self.__board.get_distance_of(self.__board.my_enemy_base, monster.pos) < 4000 :
    #             if self.__board.get_distance_of(hero.pos, monster.pos) < Shield.RANGE and self.__game.me.mana > Action.SPELL_MANA * 2 and self.__board.get_distance_of(hero.pos, monster.pos) > Shield.RANGE :
    #                 GLogger.spell_shield(monster.id)
    #             else :
    #                 GLogger.move(monster.pos)
    #         else:
    #             GLogger.move(default_pos)
    #     else:
    #         GLogger.move(default_pos)