#!/bin/python3


# Bit Manipulation: Lonely Integer
# Cracking the Coding Interview Challenge
# https://www.hackerrank.com/challenges/ctci-lonely-integer

import sys

def lonely_integer(a):
    d = {}
    extra = None
    for i in a:
        if i not in d:
            d[i] = False
        else:
            d[i] = True
    for j in d:
        if d[j] is False:
            return j
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
