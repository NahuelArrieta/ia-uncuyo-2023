from enviroment import *
from agent import *

env = Enviroment(10,10,0.2)
env.print_environment()

agentBFS = Agent(env)
agentBFS.breadth_first_search()
print("\nVisited nodes in BFS: " + str(agentBFS.visited_nodes))

agentDFS = Agent(env)
agentDFS.depth_first_search()
print("\nVisited nodes in DFS: " + str(agentDFS.visited_nodes))