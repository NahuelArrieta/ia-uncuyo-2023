from typing import Any
from board import Solution
import random

class Selection:
    def __init__(self, func: str):
        if func == "proportional":
            self.selection = self.proportional_selection
        else:
            raise Exception("Invalid selection function")
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.proportional_selection(*args, **kwds)

    def proportional_selection(self, n, solution_list):
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