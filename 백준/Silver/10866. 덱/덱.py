import sys
from collections import deque

PUSH_FRONT = "push_front"
PUSH_BACK = "push_back"
POP_FRONT = "pop_front"
POP_BACK = "pop_back"
SIZE = "size"
EMPTY = "empty"
FRONT = "front"
BACK = "back"
input = sys.stdin.readline
n = int(input().strip())
q = deque()

for __ in range(n):
    op = input().strip().split()

    if op[0] == PUSH_FRONT:
        q.appendleft(op[1])

    elif op[0] == PUSH_BACK:
        q.append(op[1])

    elif op[0] == POP_FRONT:
        if len(q) == 0:
            print(-1)
            continue
        print(q.popleft())
    elif op[0] == POP_BACK:
        if len(q) == 0:
            print(-1)
            continue
        print(q.pop())
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