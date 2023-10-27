from typing import Any
from board import Solution
from random import random

class Replacement:
    def __init__(self, func: str):
        if func == "estilist":
            self.replacement = self.estilist_replacement
        elif func == "proportional":
            self.replacement = self.proportional_replacement
        else:
            raise Exception("Invalid replacement function")
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.replacement(*args, **kwds)
    
    def estilist_replacement(self, population, population_size):
        ## sort solutions by fitness
        population.sort(key=lambda x: x.fitness, reverse=True)
        ## return the best solutions
        return population[:population_size]

    def proportional_replacement(self, population,population_size):
        ## sort solutions by fitness
        population.sort(key=lambda x: x.fitness, reverse=True)
        ## calculate the sum of all fitness
        fitness_sum = 0
        for solution in population:
            fitness_sum += solution.fitness
        ## calculate the probability of each solution
        for solution in population:
            solution.probability = solution.fitness / fitness_sum
        ## calculate the cumulative probability of each solution
        for i in range(1, len(population)):
            population[i].probability += population[i-1].probability
        ## select the best solutions
        new_population = []
        for _ in range(self.solution.population_size):
            random_number = random.random()
            for solution in population:
                if random_number < solution.probability:
                    new_population.append(solution)
                    break
        return new_population