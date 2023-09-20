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
        ## insert in priority queue based in node.g
        if node != None:
            for i in range(len(self.queue)):
                cn = self.queue[i]
                if node.g < cn.g:
                    self.queue.insert(i, node)
                    return
            self.queue.append(node)


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
    
    def print_queue(self):
        for i in range(len(self.queue)):
            cn = self.queue[i]
            print("(" + str(cn.posX), ",", str(cn.posY), ";", str(cn.g), ")", end = " ")

    def in_queue(self, node: Node):
        for cn in self.queue:
            if cn.posX == node.posX and cn.posY == node.posY:
                return True
        return False

    ## A* Search
    def a_star_search(self):
        
        inital_node = Node(self.init_posX, self.init_posY)
        inital_node.set_g(self.env.calculate_distance_to_end(inital_node))
        self.insert(inital_node)
        while len(self.queue) > 0:
            cn = self.queue.pop(0)
            self.visited.append(cn)
            if self.env.is_end(cn):
                self.last_node = cn
                return
            if not(self.in_queue(cn)):
                self.insert(self.env.right_node(cn))
                self.insert(self.env.left_node(cn))
                self.insert(self.env.up_node(cn))
                self.insert(self.env.down_node(cn))
                # print("\n\n(", str(cn.posX), ",", str(cn.posY), "): ", end = "")
                # self.print_queue()




    
    