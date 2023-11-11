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
        

def test_tree(examples, tree):
    fp = 0
    fn = 0
    tp = 0
    tn = 0


    for example in examples:
        prediction = get_prediction(tree, example)
        
        if prediction == "yes":
            if example.classP == "yes":
                tp += 1
            else:
                fp += 1

        else:
            if example.classP == "yes":
                fn += 1
            else:
                tn += 1

    return tp, tn, fp, fn
    

def print_results(tp, tn, fp, fn):
    print("TP: " + str(tp))
    print("TN: " + str(tn))
    print("FP: " + str(fp))
    print("FN: " + str(fn))
    print("Accuracy: " + str((tp+tn)/(tp+tn+fp+fn)))
    print("Precision: " + str(tp/(tp+fp)))
    print("Recall: " + str(tp/(tp+fn)))


def print_tree_rules_aux(tree, path):

    if tree.classP != None:
        print(path + " -> " + tree.classP)
        return

    for i in range(len(tree.attribute.values)):
        value = tree.attribute.values[i]
        print_tree_rules_aux(tree.branches[i], path + " & " + tree.attribute.name + " = " + value)

def print_tree_rules(tree):
    if tree.classP != None:
        print("Always " + tree.classP)
        return

    for i in range(len(tree.attribute.values)):
        value = tree.attribute.values[i]
        print_tree_rules_aux(tree.branches[i], "If: " + tree.attribute.name + " = " + value)


