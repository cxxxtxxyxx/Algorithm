import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

if M == 0:
    print(N)
    exit(0)
wall = [False] * (N + 1)
for __ in range(M):
    s, e = map(int, input().split())
    for k in range(s, e):
        if wall[k] == False:
            wall[k] = True

print(wall.count(False) - 1)