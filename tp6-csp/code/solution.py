class Solution:
    def __init__(self, n):
        self.queens = []
        self.n = n

    def print_solution(self):
        for i in range(self.n):
            for j in range(self.n):
                if j == self.queens[i]:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

    def append_queen(self, queen):
        self.queens.append(queen)

    def pop_queen(self):
        self.queens.pop()
    
    def is_valid(self):
        for i in range(len(self.queens)):
            for j in range(i+1, len(self.queens)):
                row_queen_1 = i
                col_queen_1 = self.queens[i]
                row_queen_2 = j
                col_queen_2 = self.queens[j]

                if col_queen_1 == col_queen_2:
                    ## if two queens are in the same column then h += 1
                    return False
                
                if abs(row_queen_1 - row_queen_2) == abs(col_queen_1 - col_queen_2):
                    ## if two queens are in the same diagonal then h += 1
                    return False
        return True
    


