import random

class Solution:
    def calculate_h(self):
        ## h is the number of pairs of queens that are attacking each other
        queens = self.queens
        h = 0
        for i in range(len(queens)):
            for j in range(i+1, len(queens)):
                row_queen_1 = i
                col_queen_1 = queens[i]
                row_queen_2 = j
                col_queen_2 = queens[j]

                if col_queen_1 == col_queen_2:
                    ## if two queens are in the same column then h += 1
                    h += 1
                
                if abs(row_queen_1 - row_queen_2) == abs(col_queen_1 - col_queen_2):
                    ## if two queens are in the same diagonal then h += 1
                    h += 1
        return h

    def __init__(self, queens: list):
        self.queens = queens
        self.h = self.calculate_h()
        if self.h == 0:
            self.fitness = 2
        else:
            self.fitness = 1 / self.h
    
    def get_queens(self):
        return self.queens
    
    def are_equal(self, solution):
        return self.queens == solution.queens
    
    def get_neighbors(self):
        n = len(self.queens)
        neighbors = []
        for i in range(n):
            for j in range(n):
                if j != self.queens[i]:
                    queens = self.queens.copy()
                    queens[i] = j
                    neighbor = Solution(queens)
                    neighbors.append(neighbor)
        return neighbors

    def get_best_neighbor(self):
        neighbors = self.get_neighbors()
        best_neighbor = neighbors[0]
        best_h = best_neighbor.h
        for neighbor in neighbors:
            h = neighbor.h
            if h < best_h:
                best_neighbor = neighbor
                best_h = h
        return best_neighbor

    def get_random_neighbor(self):
        n = len(self.queens)
        neighbor = self.queens.copy()
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        while j == neighbor[i]:
            j = random.randint(0, n-1)
        neighbor[i] = j
        return Solution(neighbor)

class Board:
    def __init__(self, n):
        self.size = n

        ## randomly generate queens in different rows[i for i in range(n)]
        inital_queens = [random.randint(0, n-1) for _ in range(n)]
        self.initial_solution = Solution(inital_queens)   

  
    
    def print_board(self, queens = None):
        if queens == None:
            queens = self.initial_solution.get_queens()
        print()
        for i in range(len(queens)):
            for j in range(len(queens)):
                if j == queens[i]:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
                
            print()
