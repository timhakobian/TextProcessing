from collections import defaultdict
from itertools import groupby
import sys

"""Linear Time Complexity: O(1)"""
#Helper Function:
def orda(stri):
    if(ord(stri) >= 48 and ord(stri) <= 57):
        return True
    elif (ord(stri) >= 65 and ord(stri) <= 90):
        return True
    elif (ord(stri) >= 97 and ord(stri) <= 122):
        return True
    return False

"""Linear Time Complexity: O(N)"""
def tokenize(file):
    tokens = []
    openfile = open(file, "r")
    for x in openfile:
        n = 0
        for i,c in groupby(x, orda):
            if (i == True):
                tokens.append(''.join(c).lower())
    return tokens

"""Linear Time Complexity: O(N)"""
def computeWordFrequencies(tokens):
    map = defaultdict(int)
    for i in tokens:
        map[i] += 1
    return map

"""Polynomial Time Complexity: O(nlogn)"""
def printf(frequencies):
    for i,m in sorted(frequencies.items(), key = lambda x: (-x[1],x[0]), reverse = False):
        print(str(i) + " -> " + str(m))

t = tokenize(sys.argv[1])
u = computeWordFrequencies(t)
printf(u)
