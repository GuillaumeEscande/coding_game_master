from board import Board
from glogger import *

class MonsterFinder() :
    def __init__(self, monsters):
        self.__monsters = monsters

    @property
    def monsters(self):
        return self.__monsters

    
    def find_id(self, id):
        finded_monster = [m for m in self.__monsters if m.id == id]
        return MonsterFinder(finded_monster)   



    def find_distance(self, target, distance_min=None, distance_max=None):
        
        finded_monster = list()

        for monster in self.__monsters :
            distance = Board.get_distance_of(target, monster.pos)
            if distance_min is not None:
                if distance < distance_min:
                    continue

            if distance_max is not None:
                if distance > distance_max:
                    continue
            finded_monster.append(monster)

        return MonsterFinder(finded_monster)  


    def find_health(self, health_min=None, health_max=None):
        finded_monster = self.__monsters
        if health_min is not None:
            finded_monster = [m for m in finded_monster if m.health >= health_min]
        if health_max is not None:
            finded_monster = [m for m in finded_monster if m.health <= health_max]

        return MonsterFinder(finded_monster)  


    def find_shield(self, shield_min=None, shield_max=None):
        finded_monster = self.__monsters
        if shield_min is not None:
            finded_monster = [m for m in finded_monster if m.shield >= shield_min]
        if shield_max is not None:
            finded_monster = [m for m in finded_monster if m.shield <= shield_max]

        return MonsterFinder(finded_monster) 


    def find_controlled(self, is_controlled):
        finded_monster = [m for m in self.__monsters if m.is_controlled == is_controlled]
        return MonsterFinder(finded_monster) 


    def find_threat(self, threat_for=None):
        finded_monster = [m for m in self.__monsters
        if (threat_for is None and m.threat_for == 0)
        or (threat_for is True and m.threat_for == 1)
        or (threat_for is False and m.threat_for == 2) ]
        return MonsterFinder(finded_monster) 


    def find_target(self, target=True):
        return MonsterFinder([m for m in self.__monsters
        if (target is None and m.near_base == 0)
        or (target is True and m.near_base == 1 and m.threat_for == 1)
        or (target is False and m.near_base == 1 and m.threat_for == 2) ]) 

        
    def filter_by_id(self, ids=None):
        sorted_list = [m for m in self.__monsters if m.id not in ids]
        return MonsterFinder(sorted_list)   
        
    def order_by_distance(self, near_pos, reverse=False):
        ordered_list = Board.get_nearest(near_pos, self.__monsters)
        if reverse:
            ordered_list = ordered_list[::-1]
        return MonsterFinder(ordered_list)   

    def order_by_health(self, reverse=False):
        tmp_list = self.__monsters
        tmp_list.sort(key=lambda m: m.health, reverse=reverse)
        return MonsterFinder(tmp_list)   

    def order_by_shield(self, reverse=False):
        tmp_list = self.__monsters
        tmp_list.sort(key=lambda m: m.shield, reverse=reverse)
        return MonsterFinder(tmp_list)   

    def order_by_ratio_health_distance(self, target, reverse=False):
        tmp_list = self.__monsters
        tmp_list.sort(key=lambda m: m.health / Board.get_distance_of(target, m.pos) , reverse=reverse)
        return MonsterFinder(tmp_list)  
        
    def find_ratio_health_distance(self, target, ratio_min=None, ratio_max=None):
        
        finded_monster = list()

        for monster in self.__monsters :
            distance = Board.get_distance_of(target, monster.pos)
            ratio = monster.health / distance
            if ratio_min is not None:
                if ratio < ratio_min:
                    continue

            if ratio_max is not None:
                if ratio > ratio_max:
                    continue
            finded_monster.append(monster)

        return MonsterFinder(finded_monster) 
