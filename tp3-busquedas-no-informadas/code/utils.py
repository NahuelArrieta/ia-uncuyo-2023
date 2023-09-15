from enviroment import Node

def in_list(list, node: Node):
    
    for currentNode in list:
        if currentNode != None and currentNode.posX == node.posX and currentNode.posY == node.posY:
            return True
    return False

