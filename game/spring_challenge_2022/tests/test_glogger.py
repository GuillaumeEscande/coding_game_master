import unittest
import numpy

from glogger import GLogger



def test_move(capsys):
    GLogger.move([10, 20])
    captured = capsys.readouterr()
    assert captured.out == "MOVE 10 20 \n"

    
def test_wait(capsys):
    GLogger.wait()
    captured = capsys.readouterr()
    assert captured.out == "WAIT \n"

    
def test_spell_wind(capsys):
    GLogger.spell_wind([10, 20])
    captured = capsys.readouterr()
    assert captured.out == "SPELL WIND 10 20 \n"

    
def test_spell_shield(capsys):
    GLogger.spell_shield(34)
    captured = capsys.readouterr()
    assert captured.out == "SPELL SHIELD 34 \n"

    
def test_spell_control(capsys):
    GLogger.spell_control(34, [10, 20])
    captured = capsys.readouterr()
    assert captured.out == "SPELL CONTROL 34 10 20 \n"


def test_move_comment(capsys):
    GLogger.move([10, 20],  "comment")
    captured = capsys.readouterr()
    assert captured.out == "MOVE 10 20 comment\n"

    
def test_wait_comment(capsys):
    GLogger.wait("comment")
    captured = capsys.readouterr()
    assert captured.out == "WAIT comment\n"

    
def test_spell_wind_comment(capsys):
    GLogger.spell_wind([10, 20],  "comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL WIND 10 20 comment\n"

    
def test_spell_shield_comment(capsys):
    GLogger.spell_shield(34,  "comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL SHIELD 34 comment\n"

    
def test_spell_control_comment(capsys):
    GLogger.spell_control(34, [10, 20],  "comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL CONTROL 34 10 20 comment\n"