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
    
def usage():
    """
    Affiche les instructions d'utilisation du jeu.
    """
    print("--------------------------------")
    print("Instructions d'utilisation :")
    print("    - Pour afficher les instructions d'utilisation, appuyez sur 'h'.")
    print("    - Utilisez z, s, q, d pour déplacer les pièces.")
    print("    - Appuyez sur 'e' pour quitter le jeu.")
    print("    - Appuyez sur 'r' pour recommencer le jeu.")
    print("--------------------------------")
    
    