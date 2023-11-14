from solution import *
from backtracking import *
from forward_checking import *


# n = 20

# print("n:", n)

# print("backtracking")
# solution = start_backtracking(n)
# print("number of steps done:", solution.get_steps_done())
# solution.print_solution()


# print("forward checking")
# solution = start_forward_checking(n)
# print("number of steps done:", solution.get_steps_done())
# solution.print_solution()


def iterate(file,n):

    solution_backtracking = start_backtracking(n)
    bt_steps = solution_backtracking.get_steps_done()
    bt_time = solution_backtracking.get_time()

    solution_forward_checking = start_forward_checking(n)
    fc_steps = solution_forward_checking.get_steps_done()
    fc_time = solution_forward_checking.get_time()

    file.write(str(n)  +"," + str(bt_steps) + "," + str(fc_steps) + "," + str(bt_time) + "," + str(fc_time) + "\n")

queens = [ 4, 8, 10, 12, 15]
file = open("./tp6-csp/results.csv", "w")
file.write("n,bt_steps,fc_steps,bt_time,fc_time\n")

for n in queens:
    iterate(file, n)
file.close()


