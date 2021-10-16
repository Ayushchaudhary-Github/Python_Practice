import math
import os
import random
import re
import sys

n = 15
i = n

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
            continue
        elif i % 3 == 0:
            print("fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        else:
            print(i)


fizzBuzz(n+1)

# if __name__ == '__main__':
# n = int(raw_input().strip())

#  fizzBuzz(n)