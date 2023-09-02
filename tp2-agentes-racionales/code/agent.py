from enviroment import *

class Agent:           
    def __init__(self,env: Enviroment):
        self.posX = env.init_posX
        self.posY = env.init_posY
        self.env = env
        self.claned_slots = 0
        self.actions_done = 0

    # def up(self):
    # def down(self):      
    # def left(self):
    # def right(self):
    # def suck(self): # Limpia
    # def idle(self): # no hace nada
    # def perspective(self,env): #sensa el entorno
    # def think(self): # implementa las acciones a seguir por el agente

    def get_performance(self): 
        return self.claned_slots
    
    def print_environment(self):
        for i in range(self.env.sizeX):
            print("\n")
            for j in range(self.env.sizeY):
                ## print the agent as 'X'
                if i == self.posX and j == self.posY:
                    print("X ",  end = "")
                else:
                    print(str(self.env.chart[i][j]) + " ", end = "")
        print("\n")