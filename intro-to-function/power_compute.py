# math is a library included in python that has useful math functions
import math

def pow(base, exponent):
    return math.pow(base, exponent)

base = int (input("Enter the base: "))
expo = int (input("Enter the Exponent: "))

result = pow(base, expo)

print("The power result of", base, "to the power of", expo, "is", result)