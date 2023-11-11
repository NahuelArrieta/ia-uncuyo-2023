from decisionTree import *

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


