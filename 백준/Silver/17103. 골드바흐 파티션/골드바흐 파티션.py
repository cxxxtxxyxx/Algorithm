import sys
import math

input = sys.stdin.readline


t = int(input())


nums = [int(input()) for _ in range(t)]
_max = max(nums)
primes = [False, False] + [True] * (_max - 1)
for i in range(2, int(_max ** 0.5) + 1):
    if primes[i]:
        for j in range(i + i, _max + 1, i):
            if primes[j]:
                primes[j] = False

for num in nums:
    count = 0
    for i in range(2, num // 2 + 1):
        if primes[i] and primes[num - i]:
            count += 1
    print(count)


