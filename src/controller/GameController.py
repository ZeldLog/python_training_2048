import random
from model import Score

class GameController:

    def __init__(self, board, score, view):
        self.board = board
        self.score = score
        self.view = view
        self.player_name = ""  # Variable pour stocker le nom du joueur
        self.add_random_piece()  # Ajoute une pièce aléatoire au démarrage du jeu
        self.add_random_piece()  # Ajoute une deuxième pièce aléatoire au démarrage du jeu

    def handle_key(self, event):
        if event.char == "z":
            self.board.move_up()

        elif event.char == "s":
            self.board.move_down()

        elif event.char == "q":
            self.board.move_left()

        elif event.char == "d":
            self.board.move_right()

        else:
            return

        self.add_random_piece()  # Ajoute une pièce aléatoire après chaque mouvement
        self.view.update_board(self.board)
        
        if self.board.game_is_over():
            self.view.show_game_over()
        
    def add_random_piece(self):
        """
        Ajoute une pièce aléatoire (2 ou 4) sur le plateau de jeu.
        :param board: Le plateau de jeu.
        :param score: L'instance de la classe Score pour suivre le score.
        """
        empty_positions = [(x, y) for x in range(self.board.width) for y in range(self.board.height) if self.board.get_piece(x, y) == 0]
        if empty_positions:
            x, y = random.choice(empty_positions)
            piece = random.choice([2, 4])
            self.board.place_piece(piece, x, y)
            self.score.add_points(piece)  # Ajouter le score de la pièce placée