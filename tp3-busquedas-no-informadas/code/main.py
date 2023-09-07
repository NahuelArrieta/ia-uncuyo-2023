from enviroment import *
from agent import *

env = Enviroment(10,10,0.2)
env.print_environment()
agent = Agent(env)
agent.breadth_first_search()
print("\nVisited nodes: " + str(agent.visited_nodes))