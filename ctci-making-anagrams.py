# Strings: Making Anagrams
# Cracking the Coding Interview Challenge
# https://www.hackerrank.com/challenges/ctci-making-anagrams

import string
import math


def number_needed(a, b):
    # Dictionary of letters
    d = dict.fromkeys(string.ascii_lowercase, 0)
    
    # List of letters
    aa = list(a)
    bb = list(b)
    
    # Initialize
    aList, bList = {}, {}
    diff = 0
    for key in d:
        aList[key], bList[key] = 0, 0
        
    # Compare
    for each in aa:
        aList[each] += 1
    for each in bb:
        bList[each] += 1
    for key in aList:
        diff += math.fabs(aList[key] - bList[key])
    return int(diff)


#----------------- Provided -----------------
a = input().strip()
b = input().strip()

print(number_needed(a, b))
