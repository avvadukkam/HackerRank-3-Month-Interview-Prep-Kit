#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    res = [0, 0]
    maxScore, minScore = scores[0], scores[0]
    for i in range(len(scores)):
        if maxScore<scores[i]:
            res[0]+=1
            maxScore = scores[i]
        if minScore>scores[i]:
            res[1]+=1
            minScore = scores[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
