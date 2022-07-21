import math
import os
import random
import re
import sys
from functools import reduce

def aVeryBigSum(ar):
    return reduce(lambda x, y : x + y, ar) # Using reduce for more velocity

if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(str(result) + '\n')
