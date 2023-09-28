from hill_climbing import *
from simulated_annealing import *
from board import *

board = Board(8)
board.print_board()
max_iterations = 1000

## Hill Climbing
hill_climbing = HillClimbing(board, max_iterations)
hill_climbing.print_board()
print(hill_climbing.get_iterations())


## Simulated Annealing
simulated_annealing = SimulatedAnnealing(board, max_iterations)
simulated_annealing.print_board()
print(simulated_annealing.get_iterations())


