from board import *
from genetic_algo_utils import selection, replacement, crossover, mutation
import time

class GeneticAlgorithm:
    def in_solution_list(self, solution):
        for s in self.solution_list:
            if s.are_equal(solution):
                return True
        return False
    
    def genetic_algo(self, maxIterations):
        ## init random solutions with no repeated columns
        for _ in range(self.population_size):
            queens = []
            for i in range(self.board.size):
                queens.append(i)
            random.shuffle(queens)
            new_solution = Solution(queens)
            if not self.in_solution_list(new_solution):
                self.solution_list.append(new_solution)

        ## while not found solution and not max iterations
        while self.solution_list[0].h != 0 and self.iterations < maxIterations:
            self.best_solutions.append(self.solution_list[0])

            self.iterations += 1
            ## select parents
            number_of_parents = int(self.population_size / 2)
            parents = self.selection(number_of_parents,self.solution_list)
            ## generate children
            children = self.crossover(parents)
            ## mutate children
            children = self.mutation(children)
            ## calculate fitness
            for child in children:
                new_solution = Solution(child.get_queens())
                if not self.in_solution_list(new_solution):
                    self.solution_list.append(new_solution)
            ## select new population
            self.solution_list = self.replacement(self.solution_list, self.population_size)
            ## sort solutions by fitness
            self.solution_list.sort(key=lambda x: x.fitness, reverse=True)
        
        self.endTime = time.time()
           


    def __init__(self, board, population, maxIterations, selection: selection.Selection, replacement: replacement.Replacement, crossover: crossover.Crossover, mutation: mutation.Mutation):
        self.board = board
        self.population_size = population
        self.maxIterations = maxIterations
        self.selection = selection
        self.replacement = replacement
        self.crossover = crossover
        self.mutation = mutation
        self.solution_list = []
        self.best_solutions = []
        self.iterations = 0
        self.startTime = time.time()
        self.genetic_algo(maxIterations)

    def get_time(self):
        return self.endTime - self.startTime

    def get_last_solution(self):
        return self.solution_list[0]
    
    def get_iterations(self):
        return self.iterations

    def print_board(self):
        self.board.print_board(self.get_last_solution().get_queens())
    
    def get_h_values(self):
        return [solution.h for solution in self.best_solutions]

        

