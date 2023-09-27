from board import *

def hill_climbing(board):
    current = board
    while True:
        if Board.calculate_h(current) == 0:
            return current
        neighbors = current.get_neighbors()
        best_neighbor = Board.get_best_neighbor(neighbors)
        current = best_neighbor