from tkinter import *
from pprint import pformat
from game2048.grid_2048 import *
from game2048.command_2048 import *

TILES_BG_COLOR = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078", \
                  16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b", \
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850", \
                  1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92", \
                  8192: "#24ba63"}

TILES_FG_COLOR = {0: "#776e65", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", \
                  16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", \
                  256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", \
                  2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

TILES_FONT = {"Verdana", 40, "bold"}

global grid_size_2048
grid_size_2048=4

global frame_size
frame_size=800

global tile_width
tile_width=4

global tile_heigth
tile_heigth=tile_width/2

global font_tiles
font_tiles=("Helvetica",40)

def graphical_grid_init_2048():

    window = Tk()
    window.title("Game_2048")

    top = Toplevel(window)
    top.title("Game_2048")


    grid_game=init_game(grid_size_2048)


    background=Frame(window,relief='solid',
background="black",height=frame_size, width=frame_size)
    background.grid(row=0,column=0)

    graphical_grid=[]

    for i in range(0,grid_size_2048):
        row=[]
        for j in range(0,grid_size_2048):
            row.append(Frame(background,bd=1))
        graphical_grid.append(row)

    display_and_update_graphical_grid(graphical_grid,grid_game)



    entry = Entry(window)
    entry.bind('<Up>', move_grid(grid_game,'h'))
    entry.bind('<Down>', move_grid(grid_game,'b'))
    entry.bind('<Right>', move_grid(grid_game,'d'))
    entry.bind('<Left>', move_grid(grid_game,'g'))



    window.mainloop()

def display_and_update_graphical_grid(graphical_grid,grid_game):
    i=0
    for row in graphical_grid:
        j=0

        for element in row:
            text=str(grid_game[i][j])
            if text=='0':
                text=' '
            back_color=TILES_BG_COLOR[grid_game[i][j]]
            font_color=TILES_FG_COLOR[grid_game[i][j]]
            Label(element, text=text, bg=back_color,fg=font_color,
font=font_tiles,relief=RIDGE,
height=tile_heigth,width=tile_width).grid(row=0, column=0)



            element.grid(row=i,column=j)
            j+=1
        i+=1

def key_pressed(event):
    if event.keyCode=="UP":
        value="h"
    elif event.keyCode=="DOWN":
        value="d"
    elif event.keyCode=="RIGHT":
        value="d"
    elif event.keyCode=="LEFT":
        value="g"
    else:
        value=0
    return value


graphical_grid_init_2048()
