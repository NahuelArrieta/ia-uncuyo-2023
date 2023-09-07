import random

class Enviroment: 
    def __init__(self, sizeX, sizeY, obstacle_rate):
        self.sizeX = sizeY
        self.sizeY = sizeY

        self.chart = [[0 for _ in range(sizeX)] for _ in range(sizeY)]
        # chart[i][j] = 1 --> obstaccle, 0 --> free
        
        self.init_posX = random.randint(0,sizeX-1)
        self.init_posY = random.randint(0,sizeY-1)
        self.end_posX = random.randint(0,sizeX-1)
        self.endPosY = random.randint(0,sizeY-1)

        # Fill chart with obstacles in random positions
        obstacles = self.sizeX*self.sizeY*obstacle_rate
        while obstacles>0:
            i = random.randint(0,sizeX-1)
            j = random.randint(0,sizeY-1)
            if self.chart[i][j] == 0 and (i!=self.init_posX or j!=self.init_posY) and (i!=self.end_posX or j!=self.endPosY):
                self.chart[i][j] = 1
                obstacles -= 1

    def is_free(self, posX, posY):
        return self.chart[posX][posY] == 0

    def validate_pos(self, node):
        if node == None:
            return False
        
        posX = node[0]
        posY = node[1]
        if posX >= 0 and posX < self.sizeX:
            if posY >= 0 and posY < self.sizeY:
                if self.is_free(posX, posY):
                    return True
                
        return False
    
    def right_node(self, node):
        if not(self.validate_pos(node)):
            return None
        return (node[0], node[1]+1)
    
    def left_node(self, node):
        if not(self.validate_pos(node)):
            return None
        return (node[0], node[1]-1)
    
    def up_node(self, node):
        if not(self.validate_pos(node)):
            return None
        return (node[0]-1, node[1])
    
    def down_node(self, node):
        if not(self.validate_pos(node)):
            return None
        return (node[0]+1, node[1])

    def print_environment(self):
        for i in range(self.sizeX):
            print("\n| ", end="")
            for j in range(self.sizeY):
                ## print the agent as 'X'
                if i == self.init_posX and j == self.init_posY:
                    print("I ",  end = "")
                elif i == self.end_posX and j == self.endPosY:
                    print("X ",  end = "")
                elif self.chart[i][j] == 1:
                    print("  ",  end = "")
                else:
                    print("0 ", end = "")
            print("|", end="")