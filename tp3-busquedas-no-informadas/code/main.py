from enviroment import *
from agent import *
import multiprocessing 
# matlobplot


n = 100

class Result:
    def __init__(self, env, bfs_agent, dfs_agent, limited_dfs_agent, uc_search_agent, failed_agents):
        self.env = env
        self.bfs_agent = bfs_agent
        self.dfs_agent = dfs_agent
        self.limited_dfs_agent = limited_dfs_agent
        self.uc_search_agent = uc_search_agent
        self.failed_agents = failed_agents

def write_csv(bfs_agent, dfs_agent, limited_dfs_agent, uc_search_aget, file):
    text = str(bfs_agent.visited_nodes) + "," + str(dfs_agent.visited_nodes) + "," + str(limited_dfs_agent.visited_nodes) + "," + str(uc_search_aget.visited_nodes) + "\n"
    file.write(text)

def iterate(i):
    print("iteration: ", str(i))

    ## Create the enviroment
    env = Enviroment(n,n,0.1)
    failed_agents = 0

    ## BFS agent 
    agentBFS = Agent(env)
    agentBFS.breadth_first_search()

    ## DFS agent
    agentDFS = Agent(env)
    agentDFS.depth_first_search()

    ## Limited DFS agent
    agentLimitedDFS = Agent(env)
    agentLimitedDFS.limited_DFS(3000)
    if agentLimitedDFS.last_node == None:
        failed_agents = 1

    ## Uniform Cost Search agent
    agentUCS = Agent(env)
    agentUCS.breadth_first_search()

    print("iteration ", str(i), " finished")

    ## Return the reults
    return Result(env, agentBFS, agentDFS, agentLimitedDFS, agentUCS, failed_agents)


def printPaths(result: Result):
    env = result.env
    agentBFS = result.bfs_agent
    agentDFS = result.dfs_agent
    agentLimitedDFS = result.limited_dfs_agent
    agentUCS = result.uc_search_agent
    
    ## Print the last enviroment
    print("Start position: (" + str(env.init_posX) + "," + str(env.init_posY) + ")")
    print("End position: (" + str(env.end_posX) + "," + str(env.endPosY) + ")")
    env.print_environment()

    ## Print the last path of the agents
    print("\n \n BFS path: ")
    env.print_environment(agentBFS.get_path())

    print("\n \n DFS path: ")
    env.print_environment(agentDFS.get_path())

    print("\n \n Limited DFS path: ")
    env.print_environment(agentLimitedDFS.get_path())

    print("\n \n UCS path: ")
    env.print_environment(agentUCS.get_path())



## Create the file
file = open('./tp3-busquedas-no-informadas/results/tp3-performance.csv', 'a')

## Write the header
file.write("bfs,dfs,limited_dfs,uc_search\n")

failed_agents = 0

## Get the performance of the agents
with multiprocessing.Pool() as pool:
    results = pool.map(iterate, range(1))

for res in results:
    failed_agents += res.failed_agents
    write_csv(res.bfs_agent, res.dfs_agent, res.limited_dfs_agent, res.uc_search_agent, file)

printPaths(results[0])
print("\nFailed agents: ", str(failed_agents))







## Close the file
file.close()