from enviroment import *
from agent import *

env = Enviroment(100,100,0.1)
env.print_environment()

# agentBFS = Agent(env)
# agentBFS.breadth_first_search()
# print("\nVisited nodes in BFS: " + str(agentBFS.visited_nodes))

# agentDFS = Agent(env)
# agentDFS.depth_first_search()
# print("\nVisited nodes in DFS: " + str(agentDFS.visited_nodes))