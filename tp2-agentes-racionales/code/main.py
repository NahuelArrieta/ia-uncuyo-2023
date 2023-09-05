from enviroment import *
from agent import *

def create_agent(sizeX, sizeY, dirt_rate):
    init_posX = random.randint(0, sizeX - 1)
    init_posY = random.randint(0, sizeY - 1)
    env = Enviroment(sizeX, sizeY,init_posX,init_posY,dirt_rate)
    agent = Agent(env)  
    return agent

def write_csv(sizeX, sizeY, dirt_rate, random_agent_performance, reflexive_agent_performance, file):
    file.write(str(sizeX) + "," + str(sizeY) + "," + str(dirt_rate) + "," + str(random_agent_performance) + ","+ str (reflexive_agent_performance)+ "\n")

def meassure_performance(sizeX, sizeY, dirt_rate):
    print("\nSize: (" + str(sizeX) + ", " + str(sizeY) + ") Dirt rate: " + str(dirt_rate))
    
    iterations = 100

    # Reflexive agent 
    reflexive_agent_performance = 0
    for _ in range(iterations):
        reflexive_agent = create_agent(sizeX,sizeY,dirt_rate)
        reflexive_agent.act_reflexive()
        reflexive_agent_performance += reflexive_agent.get_performance()
    avg_reflexive_agent_performance = reflexive_agent_performance/iterations
    
    # Random agent
    random_agent_performance = 0
    for _ in range(iterations):
        random_agent = create_agent(sizeX,sizeY,dirt_rate)
        random_agent.act_random()
        random_agent_performance += random_agent.get_performance()
    avg_reflexive_agent_performance = random_agent_performance/iterations

    print("Reflexive agent performance: " + str(avg_reflexive_agent_performance))    
    print("Random agent performance: " + str(avg_reflexive_agent_performance))

    write_csv(sizeX, sizeY, dirt_rate, random_agent_performance, reflexive_agent_performance, file)
    
# Create charts of 2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128
Sizes = [2, 4, 8, 16, 32, 64, 128]

# Create dirt_rates of 0.1, 0,2 0,4, 0.8
Dirt_rates = [0.1, 0.2, 0.4, 0.8]

file = open('./tp2-agentes-racionales/results/t2-performance.csv', 'w')
file.write("sizeX,sizeY,dirt_rate,random_agent_performance,reflexive_agent_performance\n")

for size in Sizes:
    for dirt_rate in Dirt_rates:
        meassure_performance(size, size, dirt_rate)
 
file.close()