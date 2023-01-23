import sys

input = sys.stdin.readline

n = int(input())

result = [0, 1, 2, 3]

for i in range(4, 1001):
    result.append(result[i - 1] + result[i - 2])


print(result[n] % 10007)