import sys
import itertools

input = sys.stdin.readline

n = int(input())
res = list(map(int, input().split()))

result = [1] * n

for i in range(1, n):
    for j in range(i):
        if res[i] > res[j]:
            result[i] = max(result[i], result[j] + 1)


print(max(result))

