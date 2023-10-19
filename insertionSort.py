#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    m = n - 1
    store = arr[m]
    while m > 0:
        if store < arr[m - 1]:
            arr[m] = arr[m - 1]
            print(" ".join(map(str, arr)))
            m -= 1
        else:
            break
    arr[m] = store
    print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
