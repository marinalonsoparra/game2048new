### fonctionnalité 3

def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move!='d' and  move!='g' and  move!='h' and move!='b':
        print('demande invalide')
        move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move


def read_size_grid():
    n=int(input("taille de la grille"))
    while n<=1:
        print('taille invalide')
        n=int(input("taille de la grille"))
    return n


def read_grid_theme():
    i=input("choix du thème (default=0, chemistery=1, alphabet=2)")
    while i!='1' and i!='2' and i!='0' :
        print('thème invalide')
        i=input("choix du thème (default=0, chemistery=1, alphabet=2)")
    return THEMES[i]


THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}



###
###def fonction_principale():
###    if __name__ == '__main__':
###        game_play()
###        exit(1)
### si on import les fonctions de jeux_2048, cela va en trainer un bug (on appelle un dossier qui rappelle notre dossier etc...)
