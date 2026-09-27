import random
from model.structure import *
from view.affichage_textuelle import *
import sys
import tty
import termios

def getch():
    import sys
    import tty
    import termios

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def initialiser_plateau():
    """
    Initialise le plateau de jeu avec deux pièces aléatoires.
    :return: Le plateau de jeu initialisé.
    """
    board = Board(4, 4)
    for _ in range(2):
        ajouter_piece_aleatoire(board)
    return board

def ajouter_piece_aleatoire(board):
    """
    Ajoute une pièce aléatoire (2 ou 4) sur le plateau de jeu.
    :param board: Le plateau de jeu.
    """
    empty_positions = [(x, y) for x in range(board.width) for y in range(board.height) if board.get_piece(x, y) == 0]
    if empty_positions:
        x, y = random.choice(empty_positions)
        piece = random.choice([2, 4])
        board.place_piece(piece, x, y)
        board.add_score(piece)  # Ajouter le score de la pièce placée
   
   
def deplacer_haut(board):
    """
    Déplace les pièces vers le haut.
    :param board: Le plateau de jeu.
    """
    # Implémentation du déplacement vers le haut
    # Cette fonction doit être complétée pour gérer le déplacement et la fusion des pièces
    
    for y in range(1, board.height):
        for x in range(board.width):
            piece = board.get_piece(x, y)
            if piece > 0:
                board.remove_piece(x, y)
                while y > 0 and board.get_piece(x, y - 1) == 0:
                    y -= 1
            if y > 0 and board.get_piece(x, y - 1) == piece:
                board.place_piece(piece * 2, x, y - 1)
            else:
                board.place_piece(piece, x, y)
            
def deplacer_bas(board):
    """
    Déplace les pièces vers le bas.
    :param board: Le plateau de jeu.
    """
    # Implémentation du déplacement vers le bas
    # Cette fonction doit être complétée pour gérer le déplacement et la fusion des pièces
    piece_positions = [(x, y) for y in range(board.height - 1, -1, -1) for x in range(board.width)]
    
    for x, y in piece_positions:
        piece = board.get_piece(x, y)
        if piece > 0:
            board.remove_piece(x, y)
            while y < board.height - 1 and board.get_piece(x, y + 1) == 0:
                y += 1
            if y < board.height - 1 and board.get_piece(x, y + 1) == piece:
                board.place_piece(piece * 2, x, y + 1)
            else:
                board.place_piece(piece, x, y)

def deplacer_gauche(board):
    """
    Déplace les pièces vers la gauche.
    :param board: Le plateau de jeu.
    """
    # Implémentation du déplacement vers la gauche
    # Cette fonction doit être complétée pour gérer le déplacement et la fusion des pièces
    piece_positions = [(x, y) for x in range(board.width) for y in range(board.height)]
    
    for x, y in piece_positions:
        piece = board.get_piece(x, y)
        if piece > 0:
            board.remove_piece(x, y)
            while x > 0 and board.get_piece(x - 1, y) == 0:
                x -= 1
            if x > 0 and board.get_piece(x - 1, y) == piece:
                board.place_piece(piece * 2, x - 1, y)
            else:
                board.place_piece(piece, x, y)

def deplacer_droite(board):
    """
    Déplace les pièces vers la droite.
    :param board: Le plateau de jeu.
    """
    # Implémentation du déplacement vers la droite
    # Cette fonction doit être complétée pour gérer le déplacement et la fusion des pièces
    piece_positions = [(x, y) for x in range(board.width - 1, -1, -1) for y in range(board.height)]
    
    for x, y in piece_positions:
        piece = board.get_piece(x, y)
        if piece > 0:
            board.remove_piece(x, y)
            while x < board.width - 1 and board.get_piece(x + 1, y) == 0:
                x += 1
            if x < board.width - 1 and board.get_piece(x + 1, y) == piece:
                board.place_piece(piece * 2, x + 1, y)
            else:
                board.place_piece(piece, x, y)

def deplacer_pieces_by_text(board, direction):
    """
    Déplace les pièces sur le plateau de jeu dans la direction spécifiée.
    :param board: Le plateau de jeu.
    :param direction: La direction du déplacement ('up', 'down', 'left', 'right').
    """
    # Implémentation du déplacement des pièces selon la direction
    # Cette fonction doit être complétée pour gérer le déplacement et la fusion des pièces
    if direction == 'up':
        deplacer_haut(board)
    elif direction == 'down':
        deplacer_bas(board)
    elif direction == 'left':
        deplacer_gauche(board)
    elif direction == 'right':
        deplacer_droite(board)
    else:
        raise ValueError("Direction invalide. Utilisez 'up', 'down', 'left' ou 'right'.")

def deplacer_touch(board, key):
    """
    Déplace les pièces sur le plateau de jeu en fonction de la touche pressée.
    :param board: Le plateau de jeu.
    :param key: La touche pressée ('w', 's', 'a', 'd').
    """
    # Implémentation du déplacement des pièces selon la touche pressée
    # Cette fonction doit être complétée pour gérer le déplacement et la fusion des pièces
    if key == 'z':
        deplacer_haut(board)
    elif key == 's':
        deplacer_bas(board)
    elif key == 'q':
        deplacer_gauche(board)
    elif key == 'd':
        deplacer_droite(board)
    else:
        raise ValueError("Touche invalide. Utilisez 'h' pour voir les instructions d'utilisation.")
    

def game_is_over(board):
    """
    Vérifie si le jeu est terminé (aucun mouvement possible) ou 2048 est atteint.
    :param board: Le plateau de jeu.
    :return: True si le jeu est terminé, False sinon.
    """
    # Implémentation de la vérification de fin de jeu
    # Cette fonction doit être complétée pour vérifier si aucun mouvement n'est possible
    if board.is_full():
        for y in range(board.height):
            for x in range(board.width):
                piece = board.get_piece(x, y)
                if piece == 2048:
                    return True  # Le joueur a gagné
                # Vérifier les pièces adjacentes pour voir si une fusion est possible
                if (x < board.width - 1 and board.get_piece(x + 1, y) == piece) or \
                   (y < board.height - 1 and board.get_piece(x, y + 1) == piece):
                    return False  # Une fusion est possible
        return True  # Aucun mouvement possible, le jeu est terminé

def game_loop():
        """
        Boucle principale du jeu.
        """
        restart = True
        usage()  # Affiche les instructions d'utilisation du jeu
        while restart:
            restart = False
            board = initialiser_plateau()   
            while not game_is_over(board):
                affichage_textuelle_plateau(board)
                affichage_textuelle_score(board)
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
                    ajouter_piece_aleatoire(board)
                except ValueError as e:
                    print(e)
            print("Game Over! Votre score final est :", board.score)
            if not restart and input("Voulez-vous rejouer ? (o/n) : ").lower() == 'o':
                restart = True
            if restart:
                print("Redémarrage du jeu...")