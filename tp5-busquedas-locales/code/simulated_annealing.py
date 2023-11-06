from board import *
import math
import time

class SimulatedAnnealing:
    def simulated_annealing(self, board: Board, maxIterations):
        current_solution = board.initial_solution
        while len(self.solutions) < maxIterations:
            self.solutions.append(current_solution)
            neighbor = current_solution.get_random_neighbor()
            if current_solution.h == 0:
                self.endTime = time.time()
                return 
            
            delta = neighbor.h - current_solution.h
            if delta < 0:
                ## if new_neighbor.h is less than current_solution.h, new_neighbor is better
                current_solution = neighbor
            else:
                probability = math.exp(-delta/self.temperature)
                if random.random() < probability:
                    self.temperature *= self.alpha
                    current_solution = neighbor
            

    def __init__(self, board, maxIterations):
        self.board = board
        self.solutions = []
        self.temperature = 50
        self.alpha = 0.50
        self.startTime = time.time()
        self.simulated_annealing(board, maxIterations)

    def get_time(self):
        return self.endTime - self.startTime

    def get_last_solution(self):
        return self.solutions[-1]
    
    def get_iterations(self):
        return len(self.solutions)

    def print_board(self):
        self.board.print_board(self.get_last_solution().get_queens())