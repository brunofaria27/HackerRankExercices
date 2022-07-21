import math
import os
import random
import re
import sys

def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    print(' '.join(map(str, res)))
    print('\n')
