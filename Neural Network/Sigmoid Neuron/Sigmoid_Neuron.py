# Sigmoid Neuron Implementation
# List of tuple inputs and weights [input]
# Bias [bias]

import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

def perceptron(input: [(bool, int), (bool, int)], bias: int) -> float:
    return sigmoid(sum([x[0]*x[1] for x in input])+bias)

print("Large Negative wx+b: {0}".format(perceptron([(0.234,-234),(0.8, -33)], 3)))
print("Large Positive wx+b: {0}".format(perceptron([(0.234,24),(0.8, 3)], 3)))