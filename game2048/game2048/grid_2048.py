from random import randint

### fonctionnalité 1
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
            if grid[i][j]!=0 and grid[i][j]!= ' ':
                value=str(grid[i][j])
            else:
                value=' '
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



### fonctionnalité 5
def get_grid_tile_max(grid):
    return max(get_all_tiles(grid))
