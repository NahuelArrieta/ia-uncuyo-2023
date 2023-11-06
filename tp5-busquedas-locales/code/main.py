from hill_climbing import *
from simulated_annealing import *
from board import *
from genetic_algo import *

board = Board(8)
board.print_board()
max_iterations = 1000

iterations_per_algo = 2

## Hill Climbing
def iterate_hc():
    correct_solutions_hc = 0
    file = open("./tp5-busquedas-locales/results/hill_climbing.csv", "w")
    file.write("iterations,time\n")
    for _ in range(iterations_per_algo):
        hill_climbing = HillClimbing(board, max_iterations)
        if hill_climbing.get_last_solution().h == 0:
            correct_solutions_hc += 1
            iterations = hill_climbing.get_iterations()
            time = hill_climbing.get_time()
            file.write(str(iterations) + "," + str(time) + "\n")


## Simulated Annealing
def iterate_sa():
    correct_solutions_sa = 0
    file = open("./tp5-busquedas-locales/results/simulated_annealing.csv", "w")
    file.write("iterations,time\n")
    for _ in range(iterations_per_algo):
        simulated_annealing = SimulatedAnnealing(board, max_iterations)
        if simulated_annealing.get_last_solution().h == 0:
            correct_solutions_sa += 1
            iterations = simulated_annealing.get_iterations()
            time = simulated_annealing.get_time()
            file.write(str(iterations) + "," + str(time) + "\n")


## Genetic Algorithm
def iterate_ga():
    r = replacement.Replacement("estilist")
    s = selection.Selection("proportional")
    c = crossover.Crossover("one_point")
    m = mutation.Mutation("swip_queens")
    correct_solutions_ga = 0
    file = open("./tp5-busquedas-locales/results/genetic_algorithm.csv", "w")
    file.write("iterations,time\n")
    for _ in range(iterations_per_algo):
        genetic_algorithm = GeneticAlgorithm(board, 100, max_iterations, s, r, c, m)
        if genetic_algorithm.get_last_solution().h == 0:
            correct_solutions_ga += 1
            iterations = genetic_algorithm.get_iterations()
            time = genetic_algorithm.get_time()
            file.write(str(iterations) + "," + str(time) + "\n")


iterate_ga()
iterate_hc()
iterate_sa()