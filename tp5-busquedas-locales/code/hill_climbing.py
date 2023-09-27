from board import *

class HillClimbing:
    def hill_climbing(self, board: Board, maxIterations):
        current = board
        while self.iterations < maxIterations:
            if Board.calculate_h(current.queens) == 0:
                return current
            self.iterations += 1
            neighbors = current.get_neighbors()
            best_neighbor = Board.get_best_neighbor(neighbors)
            current.set_queens(best_neighbor)

    def __init__(self, board, maxIterations):
        self.board = board
        self.iterations = 0
        self.last_board = self.hill_climbing(board, maxIterations)

    def get_queens(self):
        return self.last_board.get_queens()
    
    def get_h_value(self):
        return Board.calculate_h(self.last_board.get_queens())
    
    def get_iterations(self):
        return self.iterations

    def print_last_board(self):
        self.last_board.print_board()

