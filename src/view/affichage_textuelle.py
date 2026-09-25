from model import *

def affichage_textuelle(board):
    """
    Affiche le plateau de jeu sous forme textuelle.
    :param board: Le plateau de jeu à afficher.
    """
    for row in board.grid:
        print(' '.join(str(cell) for cell in row))
    