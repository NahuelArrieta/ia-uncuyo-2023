from enviroment import *
from agent import *

def create_agent(sizeX, sizeY, dirt_rate):
    init_posX = random.randint(0, sizeX - 1)
    init_posY = random.randint(0, sizeY - 1)
    env = Enviroment(sizeX, sizeY,init_posX,init_posY,dirt_rate)
    agent = Agent(env)  
    return agent

sizeX = 4
sizeY = 4
dirt_rate = 0.5
print("Reflexive agent ")
for i in range(100):
    reflexive_agent = create_agent(sizeX,sizeY,dirt_rate)
    reflexive_agent.act_reflexive()
    reflexive_agent.print_performance()

print("Random agent ")
for i in range(100):
    random_agent = create_agent(sizeX,sizeY,dirt_rate)
    random_agent.act_random()
    random_agent.print_performance()