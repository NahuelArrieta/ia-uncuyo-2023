import random

class Node:
    def __init__ (self, posX, posY, parent = None):
        self.posX = posX
        self.posY = posY
        self.parent = parent

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

    def is_free(self, node: Node):
        posX = node.posX
        posY = node.posY
        return self.chart[posX][posY] == 0

    def is_end(self, node: Node):
        if node == None:
            return False
        posX = node.posX
        posY = node.posY
        return (posX == self.end_posX and posY == self.endPosY)

    def validate_pos(self, node: Node):
        if node == None:
            return False
        
        posX = node.posX
        posY = node.posY
        if posX >= 0 and posX < self.sizeX:
            if posY >= 0 and posY < self.sizeY:
                if self.is_free(node):
                    return True
                
        return False
    
    def right_node(self, node: Node):
        newNode = Node(node.posX, node.posY+1, node)
        if not(self.validate_pos(newNode)):
            return None
        return (newNode)
    
    def left_node(self, node):
        newNode = Node(node.posX, node.posY-1, node)
        if not(self.validate_pos(newNode)):
            return None
        return (newNode)
    
    def up_node(self, node):
        newNode = Node(node.posX-1, node.posY, node)
        if not(self.validate_pos(newNode)):
            return None
        return (newNode)
    
    def down_node(self, node):
        newNode = Node(node.posX+1, node.posY, node)
        if not(self.validate_pos(newNode)):
            return None
        return (newNode)

    def print_environment(self):
        for i in range(self.sizeX):
            print("\n|", end="")
            for j in range(self.sizeY):
                ## print the agent as 'X'
                if i == self.init_posX and j == self.init_posY:
                    print("I",  end = "")
                elif i == self.end_posX and j == self.endPosY:
                    print("X",  end = "")
                elif self.chart[i][j] == 1:
                    print(" ",  end = "")
                else:
                    print("█", end = "")
            print("|", end="")

