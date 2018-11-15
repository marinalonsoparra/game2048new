### fonctionnalité 3

def read_player_command():
    move=0
    while move!='d' or 'f' or 'h' or 'b':
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
        return move


def read_size_grid():
    n=int(input("taille de la grille"))
    return n








