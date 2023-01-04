import sys
import math
from functools import reduce

input = sys.stdin.readline

def isPrime(num):
    if(num == 1):
        return False
    for idx in range(2, int(math.sqrt(num)) + 1):
        if(num % idx == 0):
            return False
    return True


while True:
    n = int(input())
    if n == 0:
        break

    a = 3
    b = n - a

    while a <= b:

        if isPrime(a) and isPrime(b):
            print(f'{n} = {a} + {b}')
            break
        
        else:
            a += 2
            b -= 2

            if a > b:
                print("Goldbach's conjecture is wrong.")
                break
   

