import sys

input = sys.stdin.readline

N = int(input())
costs = [int(input()) for __ in range(N)]

costs.sort(reverse=True)

result = 0

for i in range(N):
    if i % 3 == 2:
        continue
    
    result += costs[i]

print(result)