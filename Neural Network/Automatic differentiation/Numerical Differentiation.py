from decimal import *
import math

def xsqrd(x) -> Decimal:
    return x*x

def xqub(x) -> Decimal:
    return x*x*x

def sigmoid(x) -> Decimal:
    return Decimal(1)/Decimal(1+math.exp(-x))

def secant_estimate(function, input: Decimal):
    dx = Decimal('1E-10')#Decimal(input * Decimal(math.sqrt(sys.float_info.epsilon)))
    return (function(input + dx) - function(input))/Decimal(dx) #(function(input + dx) - function(input - dx))/(2*dx)

print(secant_estimate(xsqrd, 2))
