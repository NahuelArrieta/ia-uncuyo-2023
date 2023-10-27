from solution import *

## solve n queens problem using backtracking
def do_backtracking(solution: Solution):
    solution.increase_steps_done()
    
    ## if solution is complete return True
    if solution.is_complete():
        return True
    
    ## get first row without a queen
    for row in range(solution.n):
        if solution.rows[row].column == None:
            break
    
    ## try to add a queen in each column
    for column in range(solution.n):
        solution.add_queen(row, column)
        if solution.is_valid():
            if do_backtracking(solution):
                return True
        solution.remove_queen(row, column)
    return False

    
def start_backtracking(n):
    solution = Solution(n)
    do_backtracking(solution)
    return solution