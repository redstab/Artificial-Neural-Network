from decimal import *
import time, math, sys

def xsqrd(x) -> Decimal:
    return x*x

def xqub(x) -> Decimal:
    return x*x*x

def sigmoid(x) -> Decimal:
    return Decimal(1)/Decimal(1+math.exp(-x))

def sig_der(x):
    return math.exp(x)/((1+math.exp(x))**2)

def initiliazation():
    #global dx
    getcontext().prec = 100
    #dx = Decimal("1E-100")
    print(1)
def secant_estimate(function, input):
    dx = Decimal('1E-10')#Decimal(input * Decimal(math.sqrt(sys.float_info.epsilon)))
    return (function(input + dx) - function(input))/Decimal(dx)

def secant_estimate2(function, input):
    dx = Decimal("1E-20")
    return (function(input + dx) - function(input - dx))/(2*dx)



initiliazation()
print("Secant Estimate {}".format(secant_estimate(sigmoid, Decimal(0.5))))
print(sig_der(0.5))
