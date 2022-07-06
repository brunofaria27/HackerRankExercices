import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    new_array = list()
    for q in queries:
        ress = [s for s in strings if s == q] # List Comprehension - so this is the list of items in the strings where the element is equal to the current query
        new_array.append(len(ress))
    return ress

if __name__ == '__main__':
    strings_count = int(input().strip())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    res = matchingStrings(strings, queries)
    print('\n'.join(map(str, res)))
    print('\n')
