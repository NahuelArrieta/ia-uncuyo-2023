from solution import *


## use less_restrictive_value heuristic
def do_forward_checking(solution: Solution):
    solution.increase_steps_done()
    
    ## if solution is complete return True
    if solution.is_complete():
        return True
    
    ## get less restrictive row
    less_restrictive_row = solution.get_less_restrictive_row()
    row = less_restrictive_row.index
    
    ## try to add a queen in each column
    for column in range(solution.n):
        solution.add_queen(row, column)
        if solution.is_valid():
            if do_forward_checking(solution):
                return True
        solution.remove_queen(row, column)
    return False

def start_forward_checking(n):
    solution = Solution(n)
    do_forward_checking(solution)
    solution.set_end_time()
    return solution