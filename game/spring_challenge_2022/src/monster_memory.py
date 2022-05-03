from board import Board
from glogger import *
from monster_finder import *

class MonsterMemory() :
    BORDER_RANGE_TWIN = 200
    def __init__(self):
        self.__monsters = list()

    @property
    def monsters(self):
        return self.__monsters

        
    def update(self, new_monsters, heros):
        finded = False
        
        for new_monstre in new_monsters :
            for index, old_monster in enumerate(self.__monsters) :
                if new_monstre.id == old_monster.id :
                    self.__monsters[index] = new_monstre
                    finded = True
                    continue
            if not finded:
                GLogger.debug("New monstre ", new_monstre.id, " detected", new_monstre.__dict__)
                self.__monsters.append(new_monstre)
                
                #Si a moins de 200 du bords et direction entrante, on met le symétrique
                if abs(4500 - new_monstre.pos[1] > 4500 - MonsterMemory.BORDER_RANGE_TWIN):
                    new_id = new_monstre.id + 1
                    # Si pair, -1, si Pair, +1
                    if new_monstre.id % 2 :
                        new_id = new_monstre.id - 1

                    if new_monstre.id not in [m.id for m in self.__monsters] :

                        pos = numpy.array([
                            abs(17630 - new_monstre.pos[0]),
                            abs(9000 - new_monstre.pos[1])
                            ])

                        threat_for = 0
                        if new_monstre.threat_for == 1:
                            threat_for = 2
                        elif new_monstre.threat_for == 2:
                            threat_for = 1

                        monster = Monster(new_id, pos, 0, False, new_monstre.health, new_monstre.traj * -1, new_monstre.near_base, threat_for)
                        self.__monsters.append(monster) 
                        GLogger.debug("Newly arrived_monster  create a temporary one to simulate twin ", monster.__dict__)
            
        # Check hero visibility
        monster_finder = MonsterFinder(self.__monsters)
        new_monsters_id = [m.id for m in new_monsters]
        monster_to_delete_id = list()
        for hero in heros:
            vis_monster = monster_finder.find_distance(hero.pos, distance_max=Hero.VISIBILITY).monsters
            for monster in vis_monster:
                if monster.id not in new_monsters_id:
                    monster_to_delete_id.append(monster.id)
                    
        GLogger.debug("Deleted monsters ", monster_to_delete_id)
        
        self.__monsters = [m for m in self.__monsters if m.id not in monster_to_delete_id]





    def play_turn(self):
        # upgrade trajectoire
        for monstre in self.__monsters :
            monstre.move_turn()

        # Check hors zone
        self.__monsters = [m for m in self.__monsters if Board.is_in_board(m.pos)]

        GLogger.debug("play_turn result : ", [m.id for m in self.__monsters])
        

        

