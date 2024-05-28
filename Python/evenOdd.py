import math
import os

"""
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

"""

def CheckNumber(n):
    if n//2 != 0:
        print("Weird")
    elif n//2 == 0 and n in range(2,5):
        print("Not Weird")
    elif n//2 == 0 and n in range(6,20):
        print("Weird")
    elif n//2 == 0 and n > 20:
        print("Not weird")
    else:
        print("Give Correct Input")
        
n = 10
print(CheckNumber(n))

        
    

