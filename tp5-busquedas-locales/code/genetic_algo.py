from board import *

class GeneticAlgorithm:
    def in_solution_list(self, solution):
        for s in self.solution_list:
            if s.are_equal(solution):
                return True
        return False
    
    ## return 2 parents
    def proportional_selection(self, n):
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
        for _ in range(n):
            random_number = random.random()
            for solution in solution_list:
                if random_number < solution.cumulative_probability:
                    parents.append(solution)
                    break

        return parents
    
    ## make one point crossover
    def one_point_crossover(self, parents):
        n = len(parents)
        new_solutions = []
        ## make for forom 0 to n-1 with step 2
        for i in range(0, n, 2):
            length = len(parents[0].queens)
            crossover_point = random.randint(1, length-1)
            child_1_queens = parents[i].queens[:crossover_point] + parents[1].queens[crossover_point:]
            child_2_queens = parents[i+1].queens[:crossover_point] + parents[0].queens[crossover_point:]
            new_solutions.append(Solution(child_1_queens))
            new_solutions.append(Solution(child_2_queens))
        return new_solutions
    

    def replace_solution(self, new_solutions: list):
        solution_list = self.solution_list
        ## replace some of the old solutions with random new solutions
        for i in range(len(solution_list)):
            current_solution = solution_list[i]
            probability = random.random()
            if probability > 2 * current_solution.fitness :
                other_solution = random.choice(new_solutions)
                solution_list[i] = other_solution
                new_solutions.remove(other_solution)
        self.solution_list = solution_list
            

        # solution_list = self.solution_list
        # for solution in new_solutions:
        #     if not self.in_solution_list(solution):
        #         solution_list.append(solution)
        # ## sort solutions by fitness
        # solution_list.sort(key=lambda x: x.fitness, reverse=True)
        # ## remove the worst solutions
        # self.solution_list = solution_list[:self.population_size]


    def mutate(self, child: Solution):
        n = len(child.queens)
        for i in range(n):
            random_number = random.random()
            if random_number < 0.25:
                child.queens[i] = random.randint(0, n-1)
        return child

    
    def genetic_algo(self, maxIterations):
        ## init random solutions
        for _ in range(self.population_size):
            queens = []
            for _ in range(self.board.size):
                queens.append(random.randint(0, self.board.size-1))
            self.solution_list.append(Solution(queens))
        
        while self.iterations < maxIterations:
            parents = self.proportional_selection(self.population_size)
            new_solutions = self.one_point_crossover(parents)
            self.replace_solution(new_solutions)
            ## if the best solution is the goal state, return
            for solution in self.solution_list:
                if solution.h == 0:
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
        

        

