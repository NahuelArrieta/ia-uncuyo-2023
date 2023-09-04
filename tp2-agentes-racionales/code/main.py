from enviroment import *
from agent import *

def create_agent(sizeX, sizeY, dirt_rate):
    init_posX = random.randint(0, sizeX - 1)
    init_posY = random.randint(0, sizeY - 1)
    env = Enviroment(sizeX, sizeY,init_posX,init_posY,dirt_rate)
    agent = Agent(env)  
    agent.print_environment()
    print("\n--------------------------\n")
    return agent

reflexive_agent = create_agent(100,100,0.5)
reflexive_agent.act_reflexive()
reflexive_agent.print_performance()