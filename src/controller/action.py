import random
from model.structure import *
from view.affichage_textuelle import *

def initialiser_plateau():
    """
    Initialise le plateau de jeu avec deux pièces aléatoires.
    :return: Le plateau de jeu initialisé.
    """
    board = Board(4, 4)
    for _ in range(2):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        piece = random.choice([2, 4])
        try:
            board.place_piece(piece, x, y)
        except ValueError:
            pass  # Ignore les positions hors limites
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
                print(f"Déplacement de la pièce {piece} en position ({x}, {y}) vers le haut.")
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

def deplacer_pieces(board, direction):
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
    
def game_loop():
        """
        Boucle principale du jeu.
        """
        board = initialiser_plateau()
        while True:
            affichage_textuelle(board)
            direction = input("Entrez la direction (up, down, left, right) ou 'exit' pour quitter : ")
            if direction == 'exit':
                break
            try:
                deplacer_pieces(board, direction)
                ajouter_piece_aleatoire(board)
            except ValueError as e:
                print(e)