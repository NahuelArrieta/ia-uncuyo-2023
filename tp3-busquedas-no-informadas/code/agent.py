from enviroment import *
from enum import Enum
from random import *

class Action(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Agent:           
    def __init__(self,env: Enviroment):
        self.init_posX = env.init_posX
        self.init_posY = env.init_posY
        self.env = env
        self.visited_nodes = 0
    
    # BFS
    def breadth_first_search(self):
        queue = []
        visited = []

        queue.append((self.init_posX, self.init_posY))
        
        while len(queue) > 0:
            node = queue.pop(0)
            if node == (self.env.end_posX, self.env.endPosY):
                self.visited_nodes = len(visited)
                return 
            if node not in visited and node != None:
                visited.append(node)
                queue.append(self.env.right_node(node))
                queue.append(self.env.left_node(node))
                queue.append(self.env.up_node(node))
                queue.append(self.env.down_node(node))
        
        
