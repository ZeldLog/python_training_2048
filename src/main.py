import tkinter as tk

from model.Board import Board
from model.Score import Score
from view.GameViewTkinter import GameViewTkinter
from controller.GameController import GameController


def main():
    root = tk.Tk()

    board = Board(4, 4)
    score = Score()  # Crée une instance de la classe Score pour suivre le score
    view = GameViewTkinter(root)
    controller = GameController(board, score, view)

    root.bind("<Key>", controller.handle_key)

    view.update_board(board)

    root.mainloop()


if __name__ == "__main__":
    main()