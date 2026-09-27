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
        