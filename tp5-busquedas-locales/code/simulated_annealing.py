from board import *
import math

class SimulatedAnnealing:
    def simulated_annealing(self, board: Board, maxIterations):
        current_board = board
        while self.iterations < maxIterations:
            if Board.calculate_h(current_board.queens) == 0:
                return current_board
            self.iterations += 1
            neighbor = current_board.get_random_neighbor()
            delta = Board.calculate_h(neighbor) - Board.calculate_h(current_board.queens)
            if delta < 0:
                ## if new_neighbor.h is less than current_board.h, new_neighbor is better
                current_board.set_queens(neighbor)
            else:
                probability = math.exp(-delta/self.temperature)
                if random.random() < probability:
                    self.temperature *= self.alpha
                    current_board.set_queens(neighbor)
            

    def __init__(self, board, maxIterations):
        self.board = board
        self.iterations = 0
        self.temperature = 50
        self.alpha = 0.50
        self.last_board = self.simulated_annealing(board, maxIterations)

    def get_queens(self):
        return self.last_board.get_queens()
    
    def get_h_value(self):
        return Board.calculate_h(self.last_board.get_queens())
    
    def get_iterations(self):
        return self.iterations

    def print_board(self):
        self.board.print_board()