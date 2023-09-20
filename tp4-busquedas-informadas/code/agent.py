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
        self.last_node = None
        self.queue = []
        self.visited = []

    def get_performance(self):
        return len(self.visited)

    def insert(self, node: Node):
        if node == None:
            return
        i = 0
        cn = self.queue[0]
        while cn.cost < node.cost:
            i += 1
            cn = self.queue[i]
        self.queue.insert(i+1, node)

    # PRint Path to last node
    def print_path(self):
        path = []
        node = self.last_node
        while node != None:
            path.append(node)
            node = node.parent
        while len(path) > 0:
            node = path.pop()
            print("("+str(node.posX)+","+str(node.posY)+")", end=" ")
    
    ## Get Path
    def get_path(self):
        path = []
        node = self.last_node
        while node != None:
            path.append(node)
            node = node.parent
        path.reverse()
        return path 
    
    
    ## A* Search
    def a_star_search(self):
        self.insert(Node(self.init_posX, self.init_posY))

        while len(self.queue) > 0:
            cn = self.queue.pop()
            self.visited.append(cn)
            if self.env.is_end(cn):
                self.last_node = cn
                return
            self.insert(self.env.right_node(cn))
            self.insert(self.env.left_node(cn))
            self.insert(self.env.up_node(cn))
            self.insert(self.env.down_node(cn))




    
    