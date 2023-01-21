import sys

input = sys.stdin.readline

n = int(input().strip())

result = [0] * 10001

for __ in range(n):
    result[int(input().strip())] += 1


for idx in range(len(result)):
    if result[idx] != 0:
        for __ in range(result[idx]):
            print(idx)
