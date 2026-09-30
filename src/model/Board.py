class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        
    def __str__(self):
        result = '\n'
        for row in self.grid:
            result += ' '.join(str(cell) for cell in row) + '\n'
        return result
    
    def empty_positions(self,x,y):
        return self.grid[y][x] == 0
    
    def is_full(self):
        return all(cell != 0 for row in self.grid for cell in row)

    def place_piece(self, piece, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = piece
        else:
            raise ValueError("Position out of bounds")

    def remove_piece(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 0
        else:
            raise ValueError("Position out of bounds")

    def get_piece(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            raise ValueError("Position out of bounds")
        
    def move_up(self):
        """
        Déplace les pièces vers le haut.
        """
        # Implémentation du déplacement vers le haut
        
        for y in range(1, self.height):
            for x in range(self.width):
                piece = self.get_piece(x, y)
                if piece > 0:
                    self.remove_piece(x, y)
                    while y > 0 and self.get_piece(x, y - 1) == 0:
                        y -= 1
                if y > 0 and self.get_piece(x, y - 1) == piece:
                    self.place_piece(piece * 2, x, y - 1)
                else:
                    self.place_piece(piece, x, y)
                
    def move_down(self):
        """
        Déplace les pièces vers le bas.
        """
        # Implémentation du déplacement vers le bas

        piece_positions = [(x, y) for y in range(self.height - 1, -1, -1) for x in range(self.width)]
        
        for x, y in piece_positions:
            piece = self.get_piece(x, y)
            if piece > 0:
                self.remove_piece(x, y)
                while y < self.height - 1 and self.get_piece(x, y + 1) == 0:
                    y += 1
                if y < self.height - 1 and self.get_piece(x, y + 1) == piece:
                    self.place_piece(piece * 2, x, y + 1)
                else:
                    self.place_piece(piece, x, y)

    def move_left(self):
        """
        Déplace les pièces vers la gauche.
        """
        # Implémentation du déplacement vers la gauche

        piece_positions = [(x, y) for x in range(self.width) for y in range(self.height)]
        
        for x, y in piece_positions:
            piece = self.get_piece(x, y)
            if piece > 0:
                self.remove_piece(x, y)
                while x > 0 and self.get_piece(x - 1, y) == 0:
                    x -= 1
                if x > 0 and self.get_piece(x - 1, y) == piece:
                    self.place_piece(piece * 2, x - 1, y)
                else:
                    self.place_piece(piece, x, y)

    def move_right(self):
        """
        Déplace les pièces vers la droite.
        """
        # Implémentation du déplacement vers la droite

        piece_positions = [(x, y) for x in range(self.width - 1, -1, -1) for y in range(self.height)]
        
        for x, y in piece_positions:
            piece = self.get_piece(x, y)
            if piece > 0:
                self.remove_piece(x, y)
                while x < self.width - 1 and self.get_piece(x + 1, y) == 0:
                    x += 1
                if x < self.width - 1 and self.get_piece(x + 1, y) == piece:
                    self.place_piece(piece * 2, x + 1, y)
                else:
                    self.place_piece(piece, x, y)
                    
    def game_is_over(self):
        """
        Vérifie si le jeu est terminé (aucun mouvement possible) ou 2048 est atteint.
        :param board: Le plateau de jeu.
        :return: True si le jeu est terminé, False sinon.
        """
        # Implémentation de la vérification de fin de jeu
        if self.is_full():
            for y in range(self.height):
                for x in range(self.width):
                    piece = self.get_piece(x, y)
                    if piece == 2048:
                        return True  # Le joueur a gagné
                    # Vérifier les pièces adjacentes pour voir si une fusion est possible
                    if (x < self.width - 1 and self.get_piece(x + 1, y) == piece) or \
                    (y < self.height - 1 and self.get_piece(x, y + 1) == piece):
                        return False  # Une fusion est possible
            return True  # Aucun mouvement possible, le jeu est terminé
        