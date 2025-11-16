#https://github.com/nsous/lab10-NS
#Partner 1: Nicole Sous
#Partner 2: NA
#I did both roles, as per Case's recommendation because my group partner did not answer me.


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)
    #can have negative nums

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return a / b


def logarithm(a, b):
    if a == 1 or a <= 0 or b == 0:
        raise ValueError
    return math.log(a,b)


def exp(a, b):
    return a**b




