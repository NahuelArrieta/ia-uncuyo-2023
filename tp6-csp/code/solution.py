import time

class Solution:

    class Row:
        def __init__(self,index,n):
            self.index = index
            self.column = None
            self.posible_columns = [True] * n

        def get_count_posible_columns(self):
            count = 0
            for i in range(len(self.posible_columns)):
                if self.posible_columns[i]:
                    count += 1
            return count
    
    def __init__(self, n):
        self.rows = [Solution.Row(i,n) for i in range(n)]
        self.n = n
        self.steps_done = 0
        self.start_time = time.time()

    def set_end_time(self):
        self.end_time = time.time()

    def get_time(self):
        return self.end_time - self.start_time


    def increase_steps_done(self):
        self.steps_done += 1
    
    def get_steps_done(self):
        return self.steps_done

    def print_solution(self):
        for i in range(self.n):
            for j in range(self.n):
                if j == self.rows[i].column:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()
    
    def is_valid(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                row_queen_1 = i
                col_queen_1 = self.rows[i].column
                row_queen_2 = j
                col_queen_2 = self.rows[j].column

                ## check if columns are None
                if col_queen_1 == None or col_queen_2 == None:
                    continue

                if col_queen_1 == col_queen_2:
                    ## if two queens are in the same column then h += 1
                    return False
                
                if abs(row_queen_1 - row_queen_2) == abs(col_queen_1 - col_queen_2):
                    ## if two queens are in the same diagonal then h += 1
                    return False
        return True
    
    def add_queen(self, row, column):
        self.rows[row].column = column
    
    def remove_queen(self, row, column):
        self.rows[row].column = None
        
    def calculate_possible_columns(self):
        ## set all posible columns to True
        for i in range(self.n):
            for j in range(self.n):
                self.rows[i].posible_columns[j] = True
        
        for i in range(self.n):
            ## if column is None then continue
            if self.rows[i].column != None:
                continue
        
            for j in range(self.n):
                ## check if a new solution is valid
                self.add_queen(i, j)
                if not self.is_valid():
                    self.rows[i].posible_columns[j] = False
                self.remove_queen(i, j)

    def get_less_restrictive_row(self):
        self.calculate_possible_columns()
        less_restrictive_row = self.rows[0]
        less_restrictive_count = less_restrictive_row.get_count_posible_columns()
        for row in self.rows:
            count = row.get_count_posible_columns()
            if count < less_restrictive_count:
                less_restrictive_row = row
                less_restrictive_count = count
        return less_restrictive_row


    def is_complete(self):
        for row in self.rows:
            if row.column == None:
                return False
        return True

                
       
    # def __init__(self, n):
    #     self.queens = []
    #     self.n = n

    # def print_solution(self):
    #     for i in range(self.n):
    #         for j in range(self.n):
    #             if j == self.queens[i]:
    #                 print("Q", end=" ")
    #             else:
    #                 print(".", end=" ")
    #         print()
    #     print()

    # def append_queen(self, queen):
    #     self.queens.append(queen)

    # def pop_queen(self):
    #     self.queens.pop()
    
    # def is_valid(self):
    #     for i in range(len(self.queens)):
    #         for j in range(i+1, len(self.queens)):
    #             row_queen_1 = i
    #             col_queen_1 = self.queens[i]
    #             row_queen_2 = j
    #             col_queen_2 = self.queens[j]

    #             if col_queen_1 == col_queen_2:
    #                 ## if two queens are in the same column then h += 1
    #                 return False
                
    #             if abs(row_queen_1 - row_queen_2) == abs(col_queen_1 - col_queen_2):
    #                 ## if two queens are in the same diagonal then h += 1
    #                 return False
    #     return True
    


