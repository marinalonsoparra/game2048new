###fonctionnalité 6
import numpy as np
import copy
from random import randint


 ###   for i in range(4):
 ###       for j in range(4):
 ###           if grid[i][j]==' ':
 ###               grid[i][j]=0  ###

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



"""grid=grid_add_new_tile(grid)
print(grid_to_string_with_size(grid,4))
t=move_possible(grid)
possibilities=[i for i in range(4) if t[i]==True]
m=len(possibilities)
i=randint(0,m-1)
j=possibilities[i]
print(j)"""


###fonctions utilisées


###grid
def create_grid(n=4):
   game_grid = []
   for i in range(0,n):
        game_grid.append([' ' for i in range(0,n)])
   return game_grid


def grid_add_new_tile_at_position(game_grid,i,j):
    game_grid[i][j]=2
    return game_grid


def get_value_new_tile():
    n=randint(1,10)
    if n<=9:
        return 2
    else:
        return 4

def get_all_tiles(game_grid):
    t=[]
    if game_grid==None:
        return t
    for i in game_grid:
        for j in i:
            if j==' ' :
                t.append(0)
            else:
                t.append(j)
    return t

def get_empty_tiles_positions(game_grid):
    t=[]
    for i in range(len(game_grid)):
        for j in range(len(game_grid[i])):
            if game_grid[i][j]==0 or game_grid[i][j]==' ':
                t.append((i,j))
    return t

def grid_get_value(game_grid,x,y):
    value=game_grid[x][y]
    if value==' ':
        return 0
    else:
        return value


def get_new_position(game_grid):
    empty_tiles_positions=get_empty_tiles_positions(game_grid)
    n=len(empty_tiles_positions)
    if n==0:   ####normalement n>0 car sinon on était bloqué!!!
        i=0
    else:
        i=randint(0,n-1)
    return empty_tiles_positions[i]

def grid_add_new_tile(grid):
    x,y=get_new_position(grid)
    value=get_value_new_tile()
    grid[x][y]=value
    return grid

def init_game(n=4):
    grid=create_grid(n)
    grid=grid_add_new_tile(grid)
    grid=grid_add_new_tile(grid)
    return grid

### fonctionnalité 2

def grid_to_string(grid,n):
    a=""""""
    for i in range(n):
        a += n*' ===' + '\n'
        for j in range(n):
            value=str(grid[i][j])
            a+= '| ' +value + ' '
        a+= '|' + '\n'
    a += n*' ===' + '\n'
    return a


def long_value(grid):
    m=0
    for i in grid:
        for j in i:
            if j>m:
                m=j
    return len(str(m))

def grid_to_string_with_size(grid,n):
    l=long_value(grid)
    a=""""""
    for i in range(n):
        a += n*(' ' + (l+2)*'=') + '\n'
        for j in range(n):
            value=str(grid[i][j])
            lj=len(value)
            a+= '| ' (l-lj)* ' ' + value + ' '
        a+= '|' + '\n'
    a += n*(' ' + (l+2)*'=') + '\n'
    return a


def long_value(grid):
    m=0
    for x in grid:
        for y in x:
            if len(str(y))>m:
                m=len(str(y))
    return m

def grid_to_string_with_size(grid,n):
    lvalue=long_value(grid)
    a=""""""
    for i in range(n):
        a += n*(' '+(lvalue)*'=') + '\n'
        for j in range(n):
            if grid[i][j]!=0 and grid[i][j]!= ' ':
                value=str(grid[i][j])
            else:
                value=' '
            l=len(value)
            a+= '|' +(lvalue-l)*' '+value
        a+= '|' + '\n'
    a += n*(' '+(lvalue)*'=') + '\n'
    return a


THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def long_value_with_theme(grid,i):
    THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}
    newgrid=[]
    for x in grid:
        s=[]
        for y in x:
            value=THEMES[str(i)].get(y)
            s.append(value)
        newgrid.append(s)
    return long_value(newgrid)

def grid_to_string_with_size_and_theme(grid,i,n):
    l=long_value_with_theme(grid,i)
    newgrid=[]
    for x in grid:
        s=[]
        for y in x:
            value=THEMES[str(i)].get(y)
            s.append(value)
        newgrid.append(s)
    a=grid_to_string_with_size(newgrid,n)
    return a


###mouvement

def move_row_left(ligne):
    n=len(ligne)
    ligne2=[]
    fusion=0
    for i in range(n):
        if ligne[i]!=0 and ligne[i]!=' ':
            m=len(ligne2)
            if m>=1 and ligne[i]==ligne2[m-1] and fusion==0:
                ligne2[m-1]=2*ligne[i]
                fusion=1
            else:
                ligne2.append(ligne[i])
                fusion = 0
    while len(ligne2)<n:
        ligne2.append(0)
    return ligne2


def move_row_right(ligne):
    ligne.reverse()
    ligne2=move_row_left(ligne)
    ligne2.reverse()
    return ligne2


def move_grid(grid, d):
    grid_copy=copy.deepcopy(grid)
    if d=='g':
        grid_final=[]
        for i in grid_copy:
            grid_final.append(move_row_left(i))
    elif d=='d':
        grid_final=[]
        for i in grid_copy:
            grid_final.append(move_row_right(i))
    elif d=='h':
        grid_array=np.array(grid_copy)
        grid_transpose= np.transpose(grid_array)
        grid_final_transpose=[]
        for i in grid_transpose:
            grid_final_transpose.append(move_row_left(i))
        grid_final_transpose_array=np.array(grid_final_transpose)
        grid_final_array=np.transpose(grid_final_transpose_array)
        grid_final=grid_final_array.tolist()
    elif d=='b':
        grid_array=np.array(grid_copy)
        grid_final_transpose_array= np.transpose(grid_array)
        gridt=grid_final_transpose_array.tolist()
        grid_final_transpose=[]
        for i in gridt:
            grid_final_transpose.append(move_row_right(i))
        grid_final_transpose_array=np.array(grid_final_transpose)
        grid_final_array=np.transpose(grid_final_transpose_array)
        grid_final=grid_final_array.tolist()
    return grid_final




### fonctionnalité 5
def get_grid_tile_max(grid):
    return max(get_all_tiles(grid))



### fonctionnalité 3

def read_player_command():
    move=0
    while move!='d' or 'f' or 'h' or 'b':
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
        return move


def read_size_grid():
    n=int(input("taille de la grille"))
    return n

###fonctionnalité 5
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
