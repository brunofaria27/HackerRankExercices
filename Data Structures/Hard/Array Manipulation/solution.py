# Correct solution, but uses more memory processing to see what is happening better
import math
import os
import random
import re
import sys

def createNewArray(new_array, slice_one, slice_two, number):
    counter = slice_one[0] - 1
    for x in range(slice_one[0] - 1, slice_two[0]):
        new_array[counter] = new_array[counter] + number[0]
        counter += 1
    return new_array
    
def arrayManipulation(n, queries):
    new_array = [0] * n
    for q in queries:
        slice_one = q[:1]
        slice_two = q[1:2]
        number = q[2:3]
        new_array = createNewArray(new_array, slice_one, slice_two, number)
    return max(new_array)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print(str(result) + '\n')
    