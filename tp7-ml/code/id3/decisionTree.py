
import math


class Attribute:
    def __init__(self, name):
        self.name = name
        self.values = []
    
    def add_value(self, value):
        for v in self.values:
            if value == v :
                return
        self.values.append(value)

    def b(self, q):
        if q == 0 or q == 1:
            return 0
        ## B(q) = −(q log2 q + (1 − q) log2 (1 − q))
        return -(q * math.log(q, 2) + (1 - q) * math.log(1 - q, 2))
    
    def remainder(self, examples, attribute):

        possible_values = set([ex.values[attribute.name] for ex in examples])

        res = 0
        for v in possible_values:
            ## Get the postiives and negatives for each value
            positive = [ex for ex in examples if ex.values[attribute.name] == v and ex.classP == "yes"]
            negative = [ex for ex in examples if ex.values[attribute.name] == v and ex.classP == "no"]

            pk = len(positive)
            nk = len(negative)

            if pk + nk == 0:
                continue

            res += (pk + nk)/len(examples) * self.b(pk/(pk + nk))

        return res




    def information_gain(self, examples, attribute):
        ## Get the positives and negatives
        positive = [ex for ex in examples if ex.classP == "yes"]
        negative = [ex for ex in examples if ex.classP == "no"]

        p = len(positive)
        n = len(negative)

        b = self.b(p/(p + n))
        remainder = self.remainder(examples, attribute)

        return b - remainder
    

class Node: 
    def __init__(self, attribute, classP = None):
        self.attribute = attribute
        self.values = []
        self.branches = []
        self.classP = classP
    
    def add_branch(self, value, node):
        self.values.append(value)
        self.branches.append(node)

class Example:
    def __init__(self, row: str, attributes: list):
        ## seaprate the values
        valuesStr = row.split(",")

        ## make a map of the values
        self.values = {}
        for i in range(len(valuesStr)-1):
            currentValue = valuesStr[i]
            currentAttribute = attributes[i]
            self.values[currentAttribute.name] = currentValue
            currentAttribute.add_value(currentValue)
        
        ## set the class to predict as the last value
        self.classP = valuesStr[-1]

    def print_example(self):
        print(self.values, self.classP)
    



def plurality_values(examples: list):
    values = {}
    for ex in examples:
        if ex.classP in values:
            values[ex.classP] += 1
        else:
            values[ex.classP] = 1
    
    max_value = 0
    max_key = None
    for key in values:
        if values[key] > max_value:
            max_value = values[key]
            max_key = key
    
    return max_key
        
    

def all_same_class(examples):
    first_class = examples[0].classP
    for ex in examples:
        if ex.classP != first_class:
            return False
    return True

def select_attribute(examples, attributes) -> Attribute:
    max_gain = 0
    max_attribute = None
    for attribute in attributes:
        gain = attribute.information_gain(examples, attribute)
        if gain > max_gain:
            max_gain = gain
            max_attribute = attribute
    
    return max_attribute
    

def make_tree(examples, attributes, parent_examples) -> Node:
    # if examples is empty then return P LURALITY-VALUE(parent examples)
    if len(examples) == 0:
        return plurality_values(parent_examples)
    
    # else if all examples have the same classification then return the classification
    if all_same_class(examples):
        return Node(None, examples[0].classP)

    # else if attributes is empty then return PLURALITY-VALUE(examples)
    if len(attributes) == 0:
        return plurality_values(examples)

    # Select the best attribute
    attribute = select_attribute(examples, attributes)

    # Create a new decision tree node with attribute test
    tree = Node(attribute)

    # For each possible value of attribute
    for value in attribute.values:
        # Add a new branch below node corresponding to the test attribute = value
        exs = [ex for ex in examples if ex.values[attribute.name] == value]
        atts = [att for att in attributes if att != attribute]
        subtree = make_tree(exs, atts, examples)
        tree.add_branch(value, subtree)

    return tree




    