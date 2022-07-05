import math
import os
import random
import re
import sys

def timeConversion(s):
    time_state = s[8:]
    if time_state == 'PM':
        hour = s[0:2]
        if int(hour) != 12:
            new_hour = int(hour) + 12
            return str(new_hour) + str(s[2:8])
        return s[0:8]
    else:
        hour = s[0:2]
        new_hour = int(hour) + 12
        if new_hour >= 24:
            new_hour = int(new_hour) - 24
            return  '0' + str(new_hour) + str(s[2:8])
        return s[0:8]

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result + '\n')