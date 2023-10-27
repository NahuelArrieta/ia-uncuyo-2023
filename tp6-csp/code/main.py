from solution import *
from backtracking import *
from forward_checking import *


n = 20

print("n:", n)

print("backtracking")
solution = start_backtracking(n)
print("number of steps done:", solution.get_steps_done())
solution.print_solution()


print("forward checking")
solution = start_forward_checking(n)
print("number of steps done:", solution.get_steps_done())
solution.print_solution()

