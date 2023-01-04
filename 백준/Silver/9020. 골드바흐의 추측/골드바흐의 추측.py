import sys
import math

input = sys.stdin.readline

n = int(input().strip())

def isPrime(num):
    if num == 1:
        return False

    for idx in range(2, int(math.sqrt(num)) + 1):
        if num % idx == 0:
            return False
    
    return True

def guess(num):
    if num // 2 % 2 == 0:
        a = num // 2 - 1
        b = num // 2 + 1
        try:
            while(not isPrime(a) or not isPrime(b)):
                a -= 2
                b += 2
        except Exception:
            return
        
        
        print(a, b)
        return
    
    else:
        a = num // 2
        b = num // 2
        if(isPrime(a) and isPrime(b)):
            print(a, b)
            return

        try:
            while(not isPrime(a) or not isPrime(b)):
                a -= 2
                b += 2
        except Exception:
            return
        
        print(a, b)
        return


for _ in range(n):
    num = int(input().strip())
    if(num == 4):
        print(2, 2)
        continue
    guess(num)
