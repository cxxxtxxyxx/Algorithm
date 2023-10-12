import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

Pn = "I" + "OI" * N

count = 0

for i in range(len(S)):
    if S[i : i + (2 * N + 1)] == Pn:
        count += 1

print(count)