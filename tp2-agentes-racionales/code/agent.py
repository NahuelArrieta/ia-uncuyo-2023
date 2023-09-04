from enviroment import *

class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    CLEAN = 4
    IDLE = 5

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
            self.env.clean_slot(self.posX, self.posY)
        self.actions_done += 1
    
    def idle(self):
        self.actions_done += 1
        return

    def make_random_move(self):
        num = random.randint(0, 3)
        if num == 0:
            self.up()
        elif num == 1:
            self.down()
        elif num == 2:
            self.left()
        else:
            self.right()

    def think(self): # implementa las acciones a seguir por el agente
        if self.env.is_dirty(self.posX, self.posY):
            self.suck()
        else:
            self.make_random_move()

    def get_performance(self):
        return (self.claned_slots/self.actions_done)*100
    
    def print_performance(self): 
        performance = (self.claned_slots/self.actions_done)*100
        print( str(self.claned_slots) + " slots cleaned in " + str(self.actions_done) + " actions. " + "Performance: " + str(performance))
    
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

    def act_reflexive(self):
        while self.actions_done < 1000 and self.env.dirty_slots > 0:
            self.think()

    def act_random(self):
        while self.actions_done < 1000 and self.env.dirty_slots > 0:
            num = random.randint(0, 5)
            if num == 0:
                self.up()
            elif num == 1:
                self.down()
            elif num == 2:
                self.left()
            elif num == 3:
                self.right()
            elif num == 4:
                self.suck()
            else:
                self.idle()
        