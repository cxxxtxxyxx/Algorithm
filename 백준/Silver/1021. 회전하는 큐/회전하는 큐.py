import sys
from collections import deque

input = sys.stdin.readline

q = deque()

def pop(q):
    q.popleft()
    return q

def move_left(q):
    q.append(q.popleft())
    return q

def move_right(q):
    q.appendleft(q.pop())


n, m = list(map(int, input().strip().split()))

op_list = list(map(int, input().strip().split()))
q = deque([i for i in range(1, n + 1)])

count = 0
for op in op_list:
    while True:
        if q[0] == op:
            q.popleft()
            break
        else:
            if q.index(op) <= len(q) // 2:
                q.rotate(-1)
            else:
                q.rotate(1)
            count += 1


print(count)