from solution import *

## solve n queens problem using backtracking
def do_backtracking(solution: Solution):
    ## if solution is complete return True
    if len(solution.queens) == solution.n:
        return True
    
    ## try to add a queen in each column
    for i in range(solution.n):
        solution.append_queen(i)
        if solution.is_valid():
            if do_backtracking(solution):
                return True
        solution.pop_queen()
    return False

    
def start_backtracking(n):
    solution = Solution(n)
    do_backtracking(solution)
    return solution