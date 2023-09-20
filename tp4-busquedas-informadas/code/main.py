from enviroment import *
from agent import *

def write_csv(algorithm, performance, n_env, done, file):
    file.write(algorithm + "," + str(performance) + "," + str(n_env) + "," + str(done) + "\n")

def iterate(i, file):
    print("Iteration", i)
    env = Enviroment(100, 100, 0.1)
    agent = Agent(env)

    agent.a_star_search()
    write_csv("A*", agent.get_performance(), i, env.is_end(agent.last_node), file)

def print_path():
    env = Enviroment(15, 15, 0.1)
    agent = Agent(env)

    agent.a_star_search()
    env.print_environment(agent.get_path())

file = open("./tp4-busquedas-informadas/informada-results.csv", "w")

file.write("Algorithm_name,env_n,estates_n,solution_found")

for i in range(30):
    iterate(i, file)

file.close()

print_path()
