import unittest
import numpy

from actions import *


def test_move(capsys):
    action = Move(numpy.array([10, 20]))
    action.set_comment("comment")
    captured = capsys.readouterr()
    assert captured.out == "MOVE 10 20 comment\n"

    
def test_wait(capsys):
    action = Wait()
    action.set_comment("comment")
    captured = capsys.readouterr()
    assert captured.out == "WAIT comment\n"

    
def test_spell_wind(capsys):
    action = Wind(numpy.array([10, 20]))
    action.set_comment("comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL WIND 10 20 comment\n"

    
def test_spell_shield(capsys):
    action = Shield(34)
    action.set_comment("comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL SHIELD 34 comment\n"

    
def test_spell_control(capsys):
    action = Control(34, numpy.array([10, 20]))
    action.set_comment("comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL CONTROL 34 10 20 comment\n"