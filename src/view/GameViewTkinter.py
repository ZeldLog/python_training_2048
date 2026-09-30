import tkinter as tk
from tkinter import messagebox


class GameViewTkinter:

    def __init__(self, root):
        self.root = root
        self.root.title("2048")

        self.cells = []

        for y in range(4):
            row = []

            for x in range(4):
                label = tk.Label(
                    root,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial", 24),
                    relief="solid"
                )

                label.grid(row=y, column=x, padx=2, pady=2)
                row.append(label)

            self.cells.append(row)

    def update_board(self, board):
        for y in range(board.height):
            for x in range(board.width):
                value = board.get_piece(x, y)

                self.cells[y][x].config(
                    text="" if value == 0 else str(value)
                )
                
    def show_game_over(self):
        messagebox.showinfo(
            "Game Over",
            "La partie est terminée !"
        )
        self.root.quit()  # Ferme la fenêtre principale après la partie