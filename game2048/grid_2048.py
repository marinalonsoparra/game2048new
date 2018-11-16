from random import randint
import copy
### fonctionnalité 1
def create_grid(n=4):
   game_grid = []
   for i in range(0,n):
        game_grid.append([0 for i in range(0,n)])
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
            if game_grid[i][j]==0 or game_grid[i][j]==' ' or game_grid[i][j]=='':
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

THEMES = {"0": {"name": "Default",'':"", 0: "", 2: "2", 4: "4", 8: "8", 16:
"16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024:
"1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name":
"Chemistry",'':"", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64:
"C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg",
8192: "Al"}, "2": {"name": "Alphabet",'':"", 0: "", 2: "A", 4: "B", 8: "C",
16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J",
2048: "K", 4096: "L", 8192: "M"}}


def grid_to_string(grid,long):
    #longitud=len(grid)
    longitud=long
    string=""

    row=0
    for j in range(0,2*longitud+1):

            if j%2==0:
             for i in range(longitud):
                    string=string+" ==="

            if j%2!=0:

                for i in range(0,longitud):

                    string=string+"| "+str(grid[row][i])+" "
                string=string+"|"
                row+=1

            string=string+"\n"
    return string

def long_value(grid):
    long_max=0
    elem_final=""

    for row in grid:
        for elem in row:
            if len(str(elem))>long_max:
                long_max=len(str(elem))
                elem_final=elem

    return long_max,elem_final

def grid_to_string_with_size(grid,n):
    #longitud=len(grid)
    longitud=n
    lon_tile,elem=long_value(grid)

    string=""


    tile=""
    for i in range(lon_tile+1):
        tile=tile+"="


    line=tile*longitud
    line=line+"="


    row=0
    for j in range(0,(2*longitud)+1):

            if j%2 == 0:
                string =string+line


            if j%2 != 0:

                for i in range(0,longitud):
                    string=string+tile_to_string(grid[row][i],lon_tile)
                string=string+"|"
                row+=1

            string=string+"\n"
    return string

def tile_to_string(element,lon_tile):
    string="|"
    if len(str(element))==lon_tile:
        string=string+str(str(element))
    else:
        size=lon_tile-int(len(str(element)))
        espaces=' '*size
        string=string+str(element)+espaces
    return string

def long_value_with_theme(grid,theme):
    long_max,elem=long_value(grid) #1024

    transform=theme[elem] #1024-> Be
    return len(str(transform))

def grid_to_string_with_size_and_theme(grid, theme, size):
    grid_copy=copy.deepcopy(grid)
    i=0
    for row in grid:
        j=0
        for element in row:
            if element==' ' or element=='':
                element=0

            grid_copy[i][j]=theme[element]
            j+=1
        i+=1


    string=grid_to_string_with_size(grid_copy,size)

    return string





### fonctionnalité 5
def get_grid_tile_max(grid):
    return max(get_all_tiles(grid))
















