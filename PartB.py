from itertools import groupby
import sys

"""Linear Time Complexity: O(N)"""
def tokenize(file):
    tokens = []
    openfile = open(file, "r")
    for x in openfile:
        n = 0
        for i,c in groupby(x, str.isalnum):
            if (i == True):
                tokens.append(''.join(c).lower())
    return tokens

"""Linear Time Complexity: O(N) + O(1) = O(N)"""
def intersection(file1, file2):
    similarities = set()
    temp1 = tokenize(file1)
    temp2 = tokenize(file2)
    for i in temp1:
        if i in temp2:
            similarities.add(i)
    return len(similarities)

print(intersection(sys.argv[1], sys.argv[2]))