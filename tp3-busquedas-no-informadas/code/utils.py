from enviroment import Node

def in_list(list, node: Node):
    for curretnNode in list:
        if curretnNode.posX == node.posX and curretnNode.posY == node.posY:
            return True
    return False

