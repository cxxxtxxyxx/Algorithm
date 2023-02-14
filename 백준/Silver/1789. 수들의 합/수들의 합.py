import sys

input = sys.stdin.readline

S = int(input())

i = 1

while True:
    S -= i
    i += 1

    if S < i:
        break

print(i - 1)
