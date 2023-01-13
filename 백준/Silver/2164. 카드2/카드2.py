import sys

from collections import deque

input = sys.stdin.readline

def generator(q):

    q.popleft()
    q.append(q.popleft())

    return q

n = int(input().strip())

q = deque([i for i in range(1, n + 1)])

while len(q) != 1:
    generator(q)

print(q[0])