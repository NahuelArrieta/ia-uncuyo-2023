from enviroment import *
from agent import *
import multiprocessing 
# matlobplot


n = 100





class Result:
    def __init__(self, env, bfs_agent, dfs_agent, limited_dfs_agent, uc_search_agent):
        self.env = env
        self.bfs_agent = bfs_agent
        self.dfs_agent = dfs_agent
        self.limited_dfs_agent = limited_dfs_agent
        self.uc_search_agent = uc_search_agent

def write_csv(bfs_agent, dfs_agent, limited_dfs_agent, uc_search_aget):
    file = open('./tp3-busquedas-no-informadas/results/tp3-performance.csv', 'a')
    text = str(bfs_agent.visited_nodes) + "," + str(dfs_agent.visited_nodes) + "," + str(limited_dfs_agent.visited_nodes) + "," + str(uc_search_aget.visited_nodes) + "\n"
    file.write(text)
    file.close()

def iterate(i):
    print("iteration: ", str(i))

    ## Create the enviroment
    env = Enviroment(n,n,0.1)

    ## BFS agent 
    agentBFS = Agent(env)
    agentBFS.breadth_first_search()

    ## DFS agent
    agentDFS = Agent(env)
    agentDFS.depth_first_search()

    ## Limited DFS agent
    agentLimitedDFS = Agent(env)
    agentLimitedDFS.limited_DFS(5000)

    ## Uniform Cost Search agent
    agentUCS = Agent(env)
    agentUCS.breadth_first_search()

    print("iteration ", str(i), " finished")

    ## Write the reults
    res = Result(env, agentBFS, agentDFS, agentLimitedDFS, agentUCS)
    write_csv(res.bfs_agent, res.dfs_agent, res.limited_dfs_agent, res.uc_search_agent)



def printPaths():
    ## Create the enviroment
    env = Enviroment(15,15,0.1)

    ## BFS agent 
    agentBFS = Agent(env)
    agentBFS.breadth_first_search()

    ## DFS agent
    agentDFS = Agent(env)
    agentDFS.depth_first_search()
    
    ## Print the last enviroment
    print("Start position: (" + str(env.init_posX) + "," + str(env.init_posY) + ")")
    print("End position: (" + str(env.end_posX) + "," + str(env.endPosY) + ")")
    env.print_environment()

    ## Print the last path of the agents
    print("\n \n BFS path: ")
    env.print_environment(agentBFS.get_path())

    print("\n \n DFS path: ")
    env.print_environment(agentDFS.get_path())



# with multiprocessing.Pool() as pool:
#     pool.map(iterate, range(30))

printPaths()







