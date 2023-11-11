from decisionTree import *

def get_prediction(tree: Node, example):
    ## check if the tree is a leaf
    if tree.classP != None:
        return tree.classP

    ## get the attribute of the tree
    attribute_name = tree.attribute.name 

    ## Iterate over the values of the attribute

    for i in range( len(tree.attribute.values)):
        value = tree.attribute.values[i]
        if example.values[attribute_name] == value:
            return get_prediction(tree.branches[i], example)