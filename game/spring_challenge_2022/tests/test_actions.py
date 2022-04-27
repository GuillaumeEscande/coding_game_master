import unittest
import numpy

from actions import *


def test_action(capsys):
    action = Action()
    action.set_comment("comment")
    assert action.comment == "comment"
    action.execute()
    captured = capsys.readouterr()
    assert captured.out == ""

def test_move(capsys):
    action = Move(numpy.array([10, 20]))
    action.set_comment("comment")
    action.execute()
    captured = capsys.readouterr()
    assert captured.out == "MOVE 10 20 comment\n"

def test_move_min(capsys):
    action = Move(numpy.array([-10, -20]))
    action.execute()
    captured = capsys.readouterr()
    assert captured.out == "MOVE 0 0 \n"

def test_move_max(capsys):
    action = Move(numpy.array([123456, 123456]))
    action.execute()
    captured = capsys.readouterr()
    assert captured.out == "MOVE 17630 9000 \n"

    
def test_wait(capsys):
    action = Wait()
    action.set_comment("comment")
    action.execute()
    captured = capsys.readouterr()
    assert captured.out == "WAIT comment\n"

    
def test_spell_wind(capsys):
    action = Wind(numpy.array([10, 20]))
    action.set_comment("comment")
    action.execute()
    captured = capsys.readouterr()
    assert captured.out == "SPELL WIND 10 20 comment\n"

    
def test_spell_shield(capsys):
    action = Shield(34)
    action.set_comment("comment")
    action.execute()
    captured = capsys.readouterr()
    assert captured.out == "SPELL SHIELD 34 comment\n"

    
def test_spell_control(capsys):
    action = Control(34, numpy.array([10, 20]))
    action.set_comment("comment")
    action.execute()
    captured = capsys.readouterr()
    assert captured.out == "SPELL CONTROL 34 10 20 comment\n"