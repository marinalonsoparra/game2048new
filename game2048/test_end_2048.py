###fonctionnalité 5
from pytest import *
from game2048.end_2048 import is_grid_full
from game2048.end_2048 import move_possible
from  game2048.end_2048 import is_game_over
from  game2048.end_2048 import is_game_win


def test_is_grid_full():
    assert is_grid_full([[2,4,8,2],[2,4,8,2],[2,4,8,2],[2,4,8,2]])==True

def test_move_possible():
    assert move_possible([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]) == [True,True,True,True]
    assert move_possible([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]) == [False,False,False,False]

def test_is_game_over():
    assert is_game_over([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]])==True
    assert is_game_over([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]])==False

def test_is_game_win():
    assert is_game_win([[2, 4, 8, 4096], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]])==True
    assert is_game_win([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]])==False
