from model import *

def affichage_textuelle_plateau(board):
    """
    Affiche le plateau de jeu sous forme textuelle.
    :param board: Le plateau de jeu à afficher.
    """
    for row in board.grid:
        print(' '.join(str(cell) for cell in row))
        
def affichage_textuelle_score(board):
    """
    Affiche le score actuel du plateau de jeu.
    :param board: Le plateau de jeu dont le score est affiché.
    """
    
    print("--------------------------------")
    print(f"Score actuel : {board.score}")
    print("--------------------------------")
    