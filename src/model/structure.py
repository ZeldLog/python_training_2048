class Board:
    def __init__(self, width, height):
        self.score = 0
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        
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
        
    def add_score(self, points):
        self.score += points