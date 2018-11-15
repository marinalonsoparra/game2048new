### fonctionnalité 4
import numpy as np
import copy

def move_row_left(ligne):
    n=len(ligne)
    ligne2=[]
    fusion=0
    for i in range(n):
        if ligne[i]!=0 and ligne[i]!= ' ':
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

