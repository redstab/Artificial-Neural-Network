# Perceptron Implementation
# List of tuple inputs and weights [input]
# Bias [bias]

def perceptron(input: [(bool, int), (bool, int)], bias: int) -> bool:
    return sum([x[0]*x[1] for x in input])+bias > 0

print(perceptron([(1,-2),(1, -2)], 3))