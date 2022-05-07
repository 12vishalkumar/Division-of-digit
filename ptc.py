import math
import os
import random
import re
import sys

# Complete the 'findDigits' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

def findDigits(n):
    # Write your code here
    s = str(n)
    c = 0
    for i in s:
        if(i=='0'):
            continue
        elif(int(s)%int(i) == 0):
            c += 1
        else:
            continue
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        fptr.write(str(result) + '\n')
    fptr.close()