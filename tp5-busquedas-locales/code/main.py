from hill_climbing import *
from simulated_annealing import *
from board import *
from genetic_algo import *

board = Board(16)
board.print_board()
max_iterations = 1000

iterations_per_algo = 2

## Hill Climbing
def iterate_hc():
    correct_solutions_hc = 0
    for _ in range(iterations_per_algo):
        hill_climbing = HillClimbing(board, max_iterations)
        if hill_climbing.get_last_solution().h == 0:
            correct_solutions_hc += 1
            iterations = hill_climbing.get_iterations()
            time = hill_climbing.get_time()



## Simulated Annealing
def iterate_sa():
    correct_solutions_sa = 0
    for _ in range(iterations_per_algo):
        simulated_annealing = SimulatedAnnealing(board, max_iterations)
        if simulated_annealing.get_last_solution().h == 0:
            correct_solutions_sa += 1
            iterations = simulated_annealing.get_iterations()
            time = simulated_annealing.get_time()


## Genetic Algorithm
def iterate_ga():
    r = replacement.Replacement("estilist")
    s = selection.Selection("proportional")
    c = crossover.Crossover("one_point")
    m = mutation.Mutation("swip_queens")
    correct_solutions_ga = 0
    for _ in range(iterations_per_algo):
        genetic_algorithm = GeneticAlgorithm(board, 100, max_iterations, s, r, c, m)
        if genetic_algorithm.get_last_solution().h == 0:
            correct_solutions_ga += 1
            iterations = genetic_algorithm.get_iterations()
            time = genetic_algorithm.get_time()


