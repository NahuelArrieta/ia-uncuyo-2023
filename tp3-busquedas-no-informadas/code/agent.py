from enviroment import *
from enum import Enum
from random import *
from utils import *


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
        self.last_node = None


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
    
    
    # BFS
    def breadth_first_search(self):
        queue = []
        visited = []

        queue.append(Node(self.init_posX, self.init_posY))
        
        while len(queue) > 0:
            node = queue.pop(0)
            if self.env.is_end(node):
                self.visited_nodes = len(visited)
                self.last_node = node
                return 
            if node != None and in_list(visited, node) == False and in_list(queue, node) == False:
                visited.append(node)
                queue.append(self.env.right_node(node))
                queue.append(self.env.left_node(node))
                queue.append(self.env.up_node(node))
                queue.append(self.env.down_node(node))
    
    # DFS
    def depth_first_search(self):
        stack = []
        visited = []

        stack.append(Node(self.init_posX, self.init_posY))
        
        while len(stack) > 0:
            node = stack.pop()
            if self.env.is_end(node):
                self.visited_nodes = len(visited)
                self.last_node = node
                return 
            if node != None and in_list(visited, node) == False and in_list(stack, node) == False:
                visited.append(node) 
                stack.append(self.env.down_node(node))
                stack.append(self.env.right_node(node))
                stack.append(self.env.left_node(node))
                stack.append(self.env.up_node(node))
        

    # Limited DFS
    def limited_DFS(self, limit):
        stack = []
        visited = []

        stack.append(Node(self.init_posX, self.init_posY))


        while len(stack) > 0 and len(visited) < limit:
            node = stack.pop()
            if self.env.is_end(node):
                self.visited_nodes = len(visited)
                self.last_node = node
                return 
            if node != None and in_list(visited, node) == False and in_list(stack, node) == False:
                visited.append(node)
                stack.append(self.env.down_node(node))
                stack.append(self.env.right_node(node))
                stack.append(self.env.left_node(node))
                stack.append(self.env.up_node(node))
    
    