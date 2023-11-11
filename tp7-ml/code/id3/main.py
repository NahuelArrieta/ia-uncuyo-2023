import random
from decisionTree import *
from testTree import *

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


tree = make_tree(examples, attributes[:-1], None)

## get random example
n = random.randint(0, len(examples)-1)
example = examples[n]

example.print_example()
print(get_prediction(tree, example))


