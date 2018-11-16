###fonctionnalité 6
import numpy as np
import copy
from random import randint
from game2048.command_2048 import *
from game2048.grid_2048 import *
from game2048.end_2048 import *
from game2048.textual_2048 import *





def game_play():
    n=read_size_grid()
    Themes=read_grid_theme()
    grid=init_game(n)
    print(grid_to_string_with_size_and_theme(grid,Themes,n))
    while not is_game_over(grid):
        demande=read_player_command()
        grid=move_grid(grid,demande)
        grid=grid_add_new_tile(grid)
        print(grid_to_string_with_size_and_theme(grid,Themes,n))
    if is_game_win(grid):
         print('win')
    else:
         print('game over')




def random_play():
    grid=init_game(n=4)
    print(grid_to_string_with_size(grid,4))
    while not is_game_over(grid):
        t=move_possible(grid)
        possibilities=[i for i in range(4) if t[i]==True]
        m=len(possibilities)
        i=randint(0,m-1)
        j=possibilities[i]
        if j==0:
            grid=move_grid(grid, 'g')
        if j==1:
            grid=move_grid(grid, 'd')
        if j==2:
            grid=move_grid(grid, 'h')
        if j==3:
            grid=move_grid(grid, 'b')
        grid=grid_add_new_tile(grid)
        print(grid_to_string_with_size(grid,4))
    if is_game_win(grid):
        return 'win'
    else:
        return 'game over'


