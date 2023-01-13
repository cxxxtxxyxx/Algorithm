import sys
from collections import deque


input = sys.stdin.readline

PUSH = "push"
POP = "pop"
SIZE = "size"
EMPTY = "empty"
FRONT = "front"
BACK = "back"

q = deque()

n = int(input().strip())

for __ in range(n):
    op = input().strip().split()

    if op[0] == PUSH:
        q.append(op[1])
    elif op[0] == POP:
        if len(q) == 0:
            print(-1)
            continue
        print(q.popleft())
    elif op[0] == SIZE:
        print(len(q))

    elif op[0] == EMPTY:
        if len(q) == 0:
            print(1)
            continue
        print(0)
    elif op[0] == FRONT:
        if len(q) == 0:
            print(-1)
            continue
        print(q[0])
    else:
        if len(q) == 0:
            print(-1)
            continue
        print(q[-1])