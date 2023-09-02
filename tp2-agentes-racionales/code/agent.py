from enviroment import *

class Agent:           
    def __init__(self,env: Enviroment):
        self.posX = env.init_posX
        self.posY = env.init_posY
        self.env = env
        self.claned_slots = 0
        self.actions_done = 0

    def move(self, new_posX, new_posY):
        if not(self.env.validate_pos(new_posX, new_posY)):
            return
        
        self.posX = new_posX
        self.posY = new_posY
        self.actions_done += 1

    def up(self):
        self.move(self.posX -1 , self.posY)

    def down(self):     
        self.move(self.posX +1 , self.posY)

    def left(self):
        self.move(self.posX, self.posY -1)

    def right(self):
        self.move(self.posX, self.posY +1)

    def suck(self): 
        if self.env.is_dirty(self.posX, self.posY):
            self.claned_slots += 1
        self.env.clean_slot(self.posX, self.posX)
        self.actions_done += 1
    
    def idle(self):
        return

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