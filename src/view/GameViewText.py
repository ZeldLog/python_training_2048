from model import *

def affichage_textuelle_plateau(board):
    """
    Affiche le plateau de jeu sous forme textuelle.
    :param board: Le plateau de jeu à afficher.
    """
    print(board)
        
def affichage_textuelle_score(score):
    """
    Affiche le score actuel du plateau de jeu.
    :param score: L'instance de la classe Score pour suivre le score.
    """
    
    print("--------------------------------")
    print(f"Score actuel : {score.get_score()}")
    print("--------------------------------")
    
def affichage_textuelle_high_scores(score):
    """
    Affiche les 10 meilleurs scores.
    :param score: L'instance de la classe Score pour suivre le score.
    """
    print("--------------------------------")
    print(score)
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
    
    