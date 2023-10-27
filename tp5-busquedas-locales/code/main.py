from hill_climbing import *
from simulated_annealing import *
from board import *
from genetic_algo import *

board = Board(4)
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

## Genetic Algorithm
replacement = replacement.Replacement("estilist")
selection = selection.Selection("proportional")
crossover = crossover.Crossover("one_point")
mutation = mutation.Mutation("random")

genetic_algorithm = GeneticAlgorithm(board, 100, max_iterations, selection, replacement, crossover, mutation)
genetic_algorithm.print_board()
print(genetic_algorithm.get_iterations())


