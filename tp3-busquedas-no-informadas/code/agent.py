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
    
    # DFS
    def depth_first_search(self):
        stack = []
        visited = []

        stack.append((self.init_posX, self.init_posY))
        
        while len(stack) > 0:
            node = stack.pop()
            if node == (self.env.end_posX, self.env.endPosY):
                self.visited_nodes = len(visited)
                return 
            if node not in visited and node != None:
                visited.append(node) 
                stack.append(self.env.down_node(node))
                stack.append(self.env.right_node(node))
                stack.append(self.env.left_node(node))
                stack.append(self.env.up_node(node))
        

    # Limited DFS
    def LimitedDFS(self, limit):
        stack = []
        visited = []

        stack.append((self.init_posX, self.init_posY))

        while len(stack) > 0 and len(visited) < limit:
            node = stack.pop()
            if node == (self.env.end_posX, self.env.endPosY):
                self.visited_nodes = len(visited)
                return
            if node not in visited and node != None:
                visited.append(node)
                stack.append(self.env.down_node(node))
                stack.append(self.env.right_node(node))
                stack.append(self.env.left_node(node))
                stack.append(self.env.up_node(node))
    
    # Uniform Cost Search
    def uniform_cost_search(self):
        prioriy_queue = []
        visited = []

        i = 0

        def append_by_cost(prioriy_queue, node):
            while i < len(prioriy_queue):
                if prioriy_queue[i][2] > node[2]:
                    prioriy_queue.insert(i, node)
                    return
                i += 1
                
        prioriy_queue.append((self.init_posX, self.init_posY, 0))

        while len(prioriy_queue) > 0:
            node = prioriy_queue.pop(0)
            if node == (self.env.end_posX, self.env.endPosY, 0):
                self.visited_nodes = len(visited)
                return
            if node not in visited and node != None:
                visited.append(node)
                append_by_cost(prioriy_queue,(self.env.down_node(node), node[2] + 1))
                append_by_cost(prioriy_queue,(self.env.right_node(node), node[2] + 1))
                append_by_cost(prioriy_queue,(self.env.left_node(node), node[2] + 1))
                append_by_cost(prioriy_queue,(self.env.up_node(node), node[2] + 1))