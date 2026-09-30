import random
from model.Board import Board
from model.Score import Score
from view.affichage_textuelle import affichage_textuelle_plateau, affichage_textuelle_score, usage, affichage_textuelle_high_scores
import sys
import tty
import termios

def getch():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def initialiser_plateau(score):
    """
    Initialise le plateau de jeu avec deux pièces aléatoires.
    :return: Le plateau de jeu initialisé.
    """
    board = Board(4, 4)
    for _ in range(2):
        ajouter_piece_aleatoire(board,score)
    return board

def ajouter_piece_aleatoire(board, score):
    """
    Ajoute une pièce aléatoire (2 ou 4) sur le plateau de jeu.
    :param board: Le plateau de jeu.
    :param score: L'instance de la classe Score pour suivre le score.
    """
    empty_positions = [(x, y) for x in range(board.width) for y in range(board.height) if board.get_piece(x, y) == 0]
    if empty_positions:
        x, y = random.choice(empty_positions)
        piece = random.choice([2, 4])
        board.place_piece(piece, x, y)
        score.add_points(piece)  # Ajouter le score de la pièce placée

def deplacer_touch(board, key):
    """
    Déplace les pièces sur le plateau de jeu en fonction de la touche pressée.
    :param board: Le plateau de jeu.
    :param key: La touche pressée ('w', 's', 'a', 'd').
    """
    # Implémentation du déplacement des pièces selon la touche pressée
    # Cette fonction doit être complétée pour gérer le déplacement et la fusion des pièces
    if key == 'z':
        board.move_up()
    elif key == 's':
        board.move_down()
    elif key == 'q':
        board.move_left()
    elif key == 'd':
        board.move_right()
    else:
        raise ValueError("Touche invalide. Utilisez 'h' pour voir les instructions d'utilisation.") 

def game_loop():
        """
        Boucle principale du jeu.
        """
        player_name = ""  # Variable pour stocker le nom du joueur
        score = Score()  # Crée une instance de la classe Score pour suivre le score
        score.load_high_scores()  # Charge les meilleurs scores depuis le fichier CSV
        restart = True
        usage()  # Affiche les instructions d'utilisation du jeu
        
        while restart:
            score.reset_score()  # Réinitialise le score à chaque redémarrage
            restart = False
            board = initialiser_plateau(score)   
            while not board.game_is_over():
                
                affichage_textuelle_plateau(board)
                affichage_textuelle_score(score)
                
                move = getch()
                if move == 'e':
                    print("Merci d'avoir joué !")
                    break
                if move == 'r':
                    restart = True
                    break
                if move == 'h':
                    usage()
                    continue
                try:
                    deplacer_touch(board, move)
                    ajouter_piece_aleatoire(board, score)
                except ValueError as e:
                    print(e)
                  
            if player_name == "":
                player_name = input("Entrez votre nom : ")
            else:
                new_player = input("Nouveau joueur ? (o/n) ")
                if new_player.lower() == 'o':
                    player_name = input("Entrez votre nom : ")  
            score.insert_high_score(player_name)
            affichage_textuelle_high_scores(score)
            
            if not restart and input("Voulez-vous rejouer ? (o/n) : ").lower() == 'o':
                restart = True
            if restart:
                print("Redémarrage du jeu...")
                
        score.save_high_scores()  # Sauvegarde les meilleurs scores dans le fichier CSV à la fin du jeu