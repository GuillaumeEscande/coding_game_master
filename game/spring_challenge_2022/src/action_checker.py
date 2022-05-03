import numpy
from actions import *

class ActionResult():
    def __init__(self, hit, kill):
        self.__hit = hit
        self.__kill = kill

    @property
    def hit(self):
        return self.__hit

    @property
    def kill(self):
        return self.__kill


class ActionChecker():

    def __init__(self, game, monster_finder):
        self.__monster_finder = monster_finder
        self.__game = game

    def check_action(self, action, hero):

        if self.__game.me.mana < Action.SPELL_MANA :
            return ActionResult(0, 0)

        if type(action) is Wait:
            return self._check_wait(hero)
        elif type(action) is Move:
            return self._check_move(hero, action.pos)
        elif type(action) is Wind:
            return self._check_wind(hero, action.target)
        elif type(action) is Shield:
            return self._check_shield(hero, action.id)
        elif type(action) is Control:
            return self._check_control(hero, action.id, action.target)
        return ActionResult(0, 0)

    def _check_wait(self, hero):
        hitted_monster = self.__monster_finder.find_distance(hero.pos, distance_max=Action.ATTACK_RANGE)
        hitted_monster_nb = len(hitted_monster.monsters)
        killed_monster = hitted_monster.find_health(health_max=Action.ATTACK_HIT)
        killed_monster_nb = len(killed_monster.monsters)
        return ActionResult(hitted_monster_nb, killed_monster_nb)

    def _check_move(self, hero, pos):
        real_position = Board.real_pos(hero.pos, pos, Move.RANGE)
        hitted_monster = self.__monster_finder.find_distance(real_position, distance_max=Action.ATTACK_RANGE)
        hitted_monster_nb = len(hitted_monster.monsters)
        killed_monster = hitted_monster.find_health(health_max=Action.ATTACK_HIT)
        killed_monster_nb = len(killed_monster.monsters)
        return ActionResult(hitted_monster_nb, killed_monster_nb)

    def _check_wind(self, hero, target):
        hitted_monster = self.__monster_finder.find_distance(hero.pos, distance_max=Wind.RANGE).find_shield(shield_max=0)
        hitted_monster_nb = len(hitted_monster.monsters)
        return ActionResult(hitted_monster_nb, 0)

    def _check_shield(self, hero, entity_id):
        hitted_monster = self.__monster_finder.find_id(entity_id).find_distance(hero.pos, distance_max=Shield.RANGE).find_shield(shield_max=0)
        hitted_monster_nb = len(hitted_monster.monsters)
        return ActionResult(hitted_monster_nb, 0)

    def _check_control(self, hero, entity_id, target):
        hitted_monster = self.__monster_finder.find_id(entity_id).find_distance(hero.pos, distance_max=Control.RANGE).find_shield(shield_max=0)
        hitted_monster_nb = len(hitted_monster.monsters)
        return ActionResult(hitted_monster_nb, 0)
