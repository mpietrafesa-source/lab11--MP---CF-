#https://github.com/mpietrafesa-source/lab11--MP---CF-.git
#Partner 1: Mia Pietrafesa
#Partner 2: Cameron Findley
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b
    
def subtract(a, b):
    return a - b
def sub(a,b):
    return subtract(a,b)
    
def multiply(a, b):
    return a * b
def mul(a,b):
    return multiply(a,b)

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)
def log(a,b):
    return logarithm(a,b)

def exponent(a, b):
    return a ** b
def exp(a,b):
    return exponent(a,b)

