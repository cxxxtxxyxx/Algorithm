import sys

input = sys.stdin.readline

n = int(input())

result = [0, 1, 3, 5, 11] + [0] * 996

for i in range(5, 1001):
    if i % 2 == 0:
        result[i] = (2 * result[i - 1] + 1) % 10007
    else:
        result[i] = (2 * result[i - 1] - 1) % 10007



print(result[n])