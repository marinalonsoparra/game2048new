## fonctionnalité 4

from pytest import *
from game2048.command_2048 import move_row_left
from game2048.command_2048 import move_row_right
from game2048.command_2048 import move_grid

def test_move_row_left():
    assert move_row_left([0, 0, 0, 2]) == [2, 0, 0, 0]
    assert move_row_left([0, 2, 0, 4]) == [2, 4, 0, 0]
    assert move_row_left([2, 2, 0, 4]) == [4, 4, 0, 0]
    assert move_row_left([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert move_row_left([4, 2, 0, 2]) == [4, 4, 0, 0]
    assert move_row_left([2, 0, 0, 2]) == [4, 0, 0, 0]
    assert move_row_left([2, 4, 2, 2]) == [2, 4, 4, 0]
    assert move_row_left([2, 4, 4, 0]) == [2, 8, 0, 0]
    assert move_row_left([4, 8, 16, 32]) == [4, 8, 16, 32]

def test_move_row_right():

    assert move_row_right([2, 0, 0, 0]) == [0, 0, 0, 2]
    assert move_row_right([0, 2, 0, 4]) == [0, 0, 2, 4]
    assert move_row_right([2, 2, 0, 4]) == [0, 0, 4, 4]
    assert move_row_right([2, 2, 2, 2]) == [0, 0, 4, 4]
    assert move_row_right([4, 2, 0, 2]) == [0, 0, 4, 4]
    assert move_row_right([2, 0, 0, 2]) == [0, 0, 0, 4]
    assert move_row_right([2, 4, 2, 2]) == [0, 2, 4, 4]
    assert move_row_right([2, 4, 4, 0]) == [0, 0, 2, 8]
    assert move_row_right([4, 8, 16, 32]) == [4, 8, 16, 32]

def test_move_grid():
    assert move_grid([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]],'g') == [[4,0,0,0], [8, 0, 0, 0], [16, 0, 0, 0], [4, 0, 0, 0]]
    assert move_grid([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]],'d') == [[0,0,0,4], [0, 0, 0, 8], [0, 0, 0, 16], [0, 0, 0, 4]]
    assert move_grid([[2,0,0,2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]],'h') == [[4,8,4,2], [16, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert move_grid([[2,0,0,2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]],'b') == [[0, 0, 0, 0], [0, 0, 0, 0],[4,8,0,0],[16, 2, 4, 2]]
