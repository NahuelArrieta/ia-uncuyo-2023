import random
from decisionTree import *
from testTree import *

minimum_information_gain = 0.23

## read the file
file = open("./tp7-ml/code/id3/tennis.csv", "r")
lines = file.readlines()

## the attributes are in the first line
attributesStr = lines[0].split(",")
attributesStr[-1] = attributesStr[-1].replace("\n", "")
attributes = []
for name in attributesStr:
    attributes.append(Attribute(name))

## the values are in the remaining lines
examples = []
for line in lines[1:]:
    line = line.replace("\n", "")
    examples.append(Example(line, attributes))


tree = make_tree(examples, attributes[:-1], None, minimum_information_gain)

print("\nMin information gain: " + str(minimum_information_gain))

print("\nRules of the tree:")
print_tree_rules(tree)

## get batch of random examples = 10
random_examples = random.sample(examples, 10)

## test the tree with the batch
tp, tn, fp, fn = test_tree(random_examples, tree)

## print the results}
print("\nResults:")
print_results(tp, tn, fp, fn)


