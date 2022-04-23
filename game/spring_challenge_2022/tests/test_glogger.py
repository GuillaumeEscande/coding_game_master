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

    
def test_spell(capsys):
    position = numpy.array([10, 20])
    GLogger.spell("test" , [10, 20],  "comment")
    captured = capsys.readouterr()
    assert captured.out == "SPELL test 10 20 comment\n"