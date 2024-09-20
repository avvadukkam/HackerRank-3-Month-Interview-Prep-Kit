#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    lenArr = len(arr)
    p, z, n = 0, 0, 0
    for ele in arr:
        if ele > 0:
            p += 1
        elif ele == 0:
            z += 1
        else:
            n += 1
    print('%.5f' % (p/lenArr))
    print('%.5f' % (n/lenArr))
    print("%.5f" % (z/lenArr))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
