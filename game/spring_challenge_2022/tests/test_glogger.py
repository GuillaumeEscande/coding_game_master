import unittest
import numpy

from glogger import GLogger


def test_move(capsys):
    position = numpy.array([10, 20])
    GLogger.move([10, 20],  "comment")
    captured = capsys.readouterr()
    assert captured.out == "MOVE 10 20 comment\n"

    
def test_wait(capsys):
    GLogger.wait("comment")
    captured = capsys.readouterr()
    assert captured.out == "WAIT comment\n"

    
def test_spell_wind(capsys):
    position = numpy.array([10, 20])
    GLogger.spell_wind([10, 20],  "comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL WIND 10 20 comment\n"

    
def test_spell_shield(capsys):
    position = numpy.array([10, 20])
    GLogger.spell_shield([10, 20],  "comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL SHIELD 10 20 comment\n"

    
def test_spell_control(capsys):
    position = numpy.array([10, 20])
    GLogger.spell_control(10, [10, 20],  "comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL CONTROL 10 10 20 comment\n"