from board import Solution
import random

class Mutation:
    def __init__(self, func: str):
        if func == "swip_queens":
            self.mutation = self.swip_queens
        elif func == "random":
            self.mutation = self.random_mutation
        else:
            raise Exception("Invalid mutation function")
    
    def __call__(self, *args, **kwds):
        solutions = args[0]
        for solution in solutions:
            solution.queens = self.mutation(solution.queens)
        return solutions
    
    def swip_queens(self, queens):
        n = len(queens)
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        while j == queens[i]:
            j = random.randint(0, n-1)
        queens[i] = j
        return queens

    def random_mutation(self, queens):
        n = len(queens)
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        queens[i] = j
        return queens               
