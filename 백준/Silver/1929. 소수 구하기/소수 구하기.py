import sys
import math

input = sys.stdin.readline

def isPrime(num):
    if(num == 1):
        return False
    for idx in range(2, int(math.sqrt(num)) + 1):
        if(num % idx == 0):
            return False
    return True

M, N = list(map(int, input().split(' ')))

for i in range(M, N + 1):
    if(isPrime(i) == True):
        print(i)