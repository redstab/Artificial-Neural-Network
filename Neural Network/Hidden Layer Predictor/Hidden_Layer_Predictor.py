# Uses a lot of the "rules of thumb" for the number of neurons in the hidden layers and calculates a mean of them
import math, time
from colorama import init, Fore, Back, Style

def hobs_method(nInput, nOutput, nSample, alpha):
    return nSample / (alpha * (nInput + nOutput))

def theoretical_maximum(nInput, nOutput):
    return (nInput + nOutput) * (2/3)

def total_maximum(nInput):
    return nInput * 2

def sqrt_method(nInput, nOutput):
    return math.sqrt(nInput + nOutput)

def mean(numbers):
    return float(sum(numbers))/ max(len(numbers), 1)

init() # Colorama

while(True):
    try:
        print("\033[36mSingle Hidden Layer Neuron Predictor \033[32m:>\033[0m")
        Input_Neurons =  int(input(" -  Number of Input Neurons:  "))
        Output_Neurons = int(input(" -  Number of Output Neurons: "))
        Sample_Size =    int(input(" -  Sample Size:              "))
        Alpha =          int(input(" -  Alpha Value:              "))
        print("\033[2J\033[0;H") # Clear Screen 
        break;
    except ValueError:
        print("\033[31mEnter a valid number pls\033[0m")
        time.sleep(0.5)
        print("\033[2J\033[0;0H")

hobs= hobs_method(Input_Neurons, Output_Neurons, Sample_Size, Alpha)
sqrt = sqrt_method(Input_Neurons, Output_Neurons)
thmax = theoretical_maximum(Input_Neurons, Output_Neurons)
tmax = total_maximum(Input_Neurons)

print(
"""Number of Input Neurons:     \033[32m{}\033[0m
Number of Output Neurons:    \033[35m{}\033[0m
Sample Size:                 \033[32m{}\033[0m
Alpha Value:                 \033[33m{}\033[0m

Hobs Method:         n = \033[32m{}\033[0m
Sqrt Method:         n = \033[32m{}\033[0m
Theory Maximum:      n = \033[34m{}\033[0m
Total Maximum:       n = \033[36m{}\033[0m

The number of hidden neurons is between: \033[35m[{}] \033[36m-> \033[36m[{}] \033[37mwith a predicted maximum of \033[34m[{}]
\033[37mThe best calculated prediction is: \033[92m[{}]\033[0m
""".format(Input_Neurons, Output_Neurons, Sample_Size, Alpha, hobs, sqrt, thmax, tmax, math.ceil(min(Output_Neurons, hobs, sqrt)), tmax, round(thmax), round(mean([hobs, sqrt]))))
