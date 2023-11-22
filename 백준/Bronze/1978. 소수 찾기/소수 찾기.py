import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

answer = 0

for num in nums:
    if isPrime(num):
        answer += 1

print(answer)