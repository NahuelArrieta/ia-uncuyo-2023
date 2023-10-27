from board import Solution
import random

class Crossover:
    def __init__(self, func: str):
        if func == "one_point":
            self.crossover = self.one_point_crossover
        else:
            raise Exception("Invalid crossover function")
    
    def __call__(self, *args, **kwds):
        return self.crossover(*args, **kwds)
    
    def one_point_crossover(self, parents):
        n = len(parents)
        new_solutions = []
        ## make for forom 0 to n-1 with step 2
        for i in range(0, n, 2):
            length = len(parents[0].queens)
            crossover_point = random.randint(1, length-1)
            child_1_queens = parents[i].queens[:crossover_point] + parents[i+1].queens[crossover_point:]
            child_2_queens = parents[i+1].queens[:crossover_point] + parents[i].queens[crossover_point:]
            new_solutions.append(Solution(child_1_queens))
            new_solutions.append(Solution(child_2_queens))
        return new_solutions