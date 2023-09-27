import random

class Board:
    def __init__(self, n):
        self.size = n

        ## randomly generate queens in different rows
        self.queens = [random.randint(0, n-1) for _ in range(n)]

    
    def get_queens(self):
        return self.queens
    
    def get_neighors(self):
        neighbors = []
        for i in range(self.size):
            for j in range(self.size):
                if j != self.queens[i]:
                    neighbor = self.queens.copy()
                    neighbor[i] = j
                    neighbors.append(neighbor)
        return neighbors
    
    def calculate_h(queens):
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

    def get_best_neighbor(neighbors: list):
        best_neighbor = neighbors[0]
        best_h = Board.calculate_h(best_neighbor)
        for neighbor in neighbors:
            h = Board.calculate_h(neighbor)
            if h < best_h:
                best_neighbor = neighbor
                best_h = h
        return best_neighbor