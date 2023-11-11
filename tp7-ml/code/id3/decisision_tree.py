
class Attribute:
    def __init__(self, name, values: list):
        self.name = name
        self.values = values

       

    def get_entropy(self, examples):
        # calculate the entropy of the examples
        values = {}
        for ex in examples:
            if ex.classP in values:
                values[ex.classP] += 1
            else:
                values[ex.classP] = 1
        
        entropy = 0
        for key in values:
            p = values[key] / len(examples)
            entropy -= p * math.log(p, 2)
        
        return entropy

    def information_gain(self, examples, attribute):
        # calculate the entropy of the examples
        entropy = self.get_entropy(examples)

        # calculate the sum of the entropy of the examples for each value of the attribute
        sum_entropy = 0
        for value in attribute.values:
            exs = [ex for ex in examples if ex.attribute == value]
            sum_entropy += self.get_entropy(exs)

        # calculate the information gain
        return entropy - sum_entropy
    

class Node: 
    def __init__(self, attribute)
        self.attribute = attribute
        self.branches = []
    
    def add_branch(self, node):
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
        
        ## set the class to predict as the last value
        self.classP = valuesStr[-1]

    



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
        return examples[0].classP

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
        exs = [ex for ex in examples if ex.attribute == value]
        atts = [att for att in attributes if att != attribute]
        subtree = make_tree_r(exs, atts, examples)
        tree.add_branch(subtree)

    return tree




    