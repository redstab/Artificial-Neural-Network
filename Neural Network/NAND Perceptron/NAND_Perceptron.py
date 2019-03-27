# NAND gate implemented using a perceptron
# (2 inputs + weights) + bias => binary output
# Input x1, x2
# Weights w1, w2
# Bias b

def sum_perceptron(x1, x2, w1, w2, b) -> bool:
    return ((x1*w1) + (x2*w2) + b) > 0

def nand(x1, x2) -> bool:
    """
    Using -2, -2 as weights one can implement a NAND gate from a perceptron if the bias is 3
    """
    weights = -2
    bias = 3

    return sum_perceptron(x1,x2,weights,weights,bias)

if __name__ == "__main__":
    while(True):
        x1 = int(input("x1: "))
        x2 = int(input("x2: "))
        print("-> " + str(nand(x1,x2)))