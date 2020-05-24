#Time Delta. Format from hackerrank python3, datetime strptime
#https://www.tutorialspoint.com/python/time_strptime.htm

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, fmt)
    time2 = datetime.strptime(t2, fmt)
    result = str(int(abs(time1 - time2).total_seconds()))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()
