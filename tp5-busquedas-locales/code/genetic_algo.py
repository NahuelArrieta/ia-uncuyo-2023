from board import *

class GeneticAlgorithm:
    ## return 2 parents
    def proportional_selection(self):
        solution_list = self.solution_list
        fitness_sum = 0
        for solution in solution_list:
            fitness_sum += solution.fitness
        
        ## calculate probability for each solution
        for solution in solution_list:
            solution.probability = solution.fitness / fitness_sum
        
        ## calculate cumulative probability for each solution
        solution_list[0].cumulative_probability = solution_list[0].probability
        for i in range(1, len(solution_list)):
            solution_list[i].cumulative_probability = solution_list[i].probability + solution_list[i-1].cumulative_probability

        ## select parents
        parents = []
        for _ in range(2):
            random_number = random.random()
            for solution in solution_list:
                if random_number < solution.cumulative_probability:
                    parents.append(solution)
                    break

        return parents
    
    ## make one point crossover
    def one_point_crossover(self, parents):
        n = len(parents[0].queens)
        crossover_point = random.randint(1, n-1)
        child_1 = parents[0].queens[:crossover_point] + parents[1].queens[crossover_point:]
        child_2 = parents[1].queens[:crossover_point] + parents[0].queens[crossover_point:]
        return child_1, child_2
    

    def replace_solution(self, child_1, child_2):
        solution_list = self.solution_list
        solution_list.append(Solution(child_1))
        solution_list.append(Solution(child_2))
        solution_list.sort(key=lambda x: x.h, reverse=True)
        ## remove the worst solutions
        self.solution_list = solution_list[:self.population_size]
    
    def genetic_algo(self, maxIterations):
        ## init random solutions
        for _ in range(self.population_size):
            queens = []
            for _ in range(self.board.size):
                queens.append(random.randint(0, self.board.size-1))
            self.solution_list.append(Solution(queens))
        
        while self.iterations < maxIterations:
            parents = self.proportional_selection()
            child_1, child_2 = self.one_point_crossover(parents)
            self.replace_solution(child_1, child_2)
            ## if the best solution is the goal state, return
            if self.solution_list[0].h == 0:
                return
            self.iterations += 1

    def __init__(self, board, maxIterations):
        self.board = board
        self.population_size = 10
        self.solution_list = []
        self.iterations = 0
        self.genetic_algo(maxIterations)

    def get_last_solution(self):
        return self.solution_list[0]
    
    def get_iterations(self):
        return self.iterations

    def print_board(self):
        self.board.print_board(self.get_last_solution().get_queens())
        

        

