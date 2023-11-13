from hill_climbing import *
from simulated_annealing import *
from board import *
from genetic_algo import *



max_iterations = 1000

iterations_per_algo = 30

## Hill Climbing
def iterate_hc(board, max_iterations):
    file = open("./tp5-busquedas-locales/results/" + str(board.size) +"_queens/hill_climbing.csv", "w")
    file.write("iterations,time\n")
    for _ in range(iterations_per_algo):
        hill_climbing = HillClimbing(board, max_iterations)
        if hill_climbing.get_last_solution().h == 0:
            solved = "True"
        else:
            solved = "False"
        iterations = hill_climbing.get_iterations()
        time = hill_climbing.get_time()
        file.write(str(iterations) + "," + str(time)+ "," + solved + "\n")


## Simulated Annealing
def iterate_sa(board, max_iterations):
    file = open("./tp5-busquedas-locales/results/" + str(board.size) +"_queens/simulated_annealing.csv", "w")
    file.write("iterations,time\n")
    for _ in range(iterations_per_algo):
        simulated_annealing = SimulatedAnnealing(board, max_iterations)
        if simulated_annealing.get_last_solution().h == 0:
            solved = "True"
        else:
            solved = "False"
        iterations = simulated_annealing.get_iterations()
        time = simulated_annealing.get_time()
        file.write(str(iterations) + "," + str(time)  +"," + solved + "\n")


## Genetic Algorithm
def iterate_ga(board, max_iterations):
    r = replacement.Replacement("estilist")
    s = selection.Selection("proportional")
    c = crossover.Crossover("one_point")
    m = mutation.Mutation("swip_queens")
    file = open("./tp5-busquedas-locales/results/" + str(board.size) +"_queens/genetic_algorithm.csv", "w")
    file.write("iterations,time\n")
    for _ in range(iterations_per_algo):
        genetic_algorithm = GeneticAlgorithm(board, 100, max_iterations, s, r, c, m)
        if genetic_algorithm.get_last_solution().h == 0:
            solved = "True"
        else:
            solved = "False"
        iterations = genetic_algorithm.get_iterations() +1
        time = genetic_algorithm.get_time()
        file.write(str(iterations) + "," + str(time)+ ","+ solved + "\n")

def write_h_values(algo_name, file, h_values):
    for h in h_values:
        file.write(algo_name + "," + str(h) + "\n")

# ## Iterate for each board size and algorithm
# board_sizes = [4,8,10]
# max_iterations = [500,1000,2000]
# for i in range(len(board_sizes)):
#     board = Board(board_sizes[i])
#     iterate_ga(board, max_iterations[i])
#     iterate_hc(board, max_iterations[i])
#     iterate_sa(board, max_iterations[i])




## Get the results for each algorithm
board = Board(8)
board.print_board()

file = open("./tp5-busquedas-locales/results/h_values.csv", "w")

hill_climbing = HillClimbing(board, 1000)
h_values = hill_climbing.get_h_values()
write_h_values("hill_climbing", file, h_values)

simulated_annealing = SimulatedAnnealing(board, 1000)
h_values = simulated_annealing.get_h_values()
write_h_values("simulated_annealing", file, h_values)

genetic_algorithm = GeneticAlgorithm(board, 100, 1000, selection.Selection("proportional"), replacement.Replacement("estilist"), crossover.Crossover("one_point"), mutation.Mutation("swip_queens"))
h_values = genetic_algorithm.get_h_values()
write_h_values("genetic_algorithm", file, h_values)



