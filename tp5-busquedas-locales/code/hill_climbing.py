from board import *
import time

class HillClimbing:
    def hill_climbing(self, board: Board, maxIterations):
        current_solution = board.initial_solution
        while len(self.solutions) < maxIterations:
            self.solutions.append(current_solution)
            best_neighbor = current_solution.get_best_neighbor()
            
            if best_neighbor.h >= current_solution.h or best_neighbor.h == 0:
                return 
            
            current_solution = best_neighbor
        self.endTime = time.time()

    def __init__(self, board: Board, maxIterations):
        self.board = board
        self.solutions = []
        self.startTime = time.time()
        self.hill_climbing(board, maxIterations)

    def get_time(self):
        return self.endTime - self.startTime

    def get_last_solution(self):
        return self.solutions[-1]
    
    def get_iterations(self):
        return len(self.solutions)

    def print_board(self):
        self.board.print_board(self.get_last_solution().get_queens())

