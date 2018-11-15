###fonctionnalité 5
from game2048.grid_2048 import get_empty_tiles_positions
from game2048.command_2048 import move_grid
from game2048.grid_2048 import get_grid_tile_max


def is_grid_full(grid):
    t=get_empty_tiles_positions(grid)
    return len(t)==0

def move_possible(grid):
    t=[True,True,True,True]
    if move_grid(grid,'g')==grid:
        t[0]=False
    if move_grid(grid,'d')==grid:
        t[1]=False
    if move_grid(grid,'h')==grid:
        t[2]=False
    if move_grid(grid,'b')==grid:
        t[3]=False
    return t

def is_game_over(grid):
    if is_grid_full(grid) and move_possible(grid)==[False,False,False,False]:
        return True
    else:
        return False


def is_game_win(grid):
    if is_game_over(grid):
        if get_grid_tile_max(grid)>=2048:
            return True
        else:
            return False
