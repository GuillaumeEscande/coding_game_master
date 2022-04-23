import unittest
import numpy

from cglogger import CGLogger

def test_print(capsys):
    CGLogger.print("test")
    captured = capsys.readouterr()
    assert captured.out == "test\n"

def test_debug(capsys):
    CGLogger.debug("test")
    captured = capsys.readouterr()
    assert captured.err == "test\n"