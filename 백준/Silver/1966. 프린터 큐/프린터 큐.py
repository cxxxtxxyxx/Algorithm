from collections import deque
import sys
import copy
import itertools

input = sys.stdin.readline

n = int(input())
for __ in range(n):
    count = 1
    n, m = list(map(int, input().split()))
    _priority = deque(list(map(int, input().split())))
    _priority[m] = _priority[m] * -1

    while True and _priority:
        if len(_priority) == 1 and _priority[0] < 0:
            print(count)
            break

        new_p = list(itertools.islice(_priority, 1, len(_priority)))
        if abs(_priority[0]) < abs(max(list(map(abs, new_p)))):
            _priority.rotate(-1)
        else:
            if _priority[0] < 0:
                print(count)
                break
            else:
                count += 1
                _priority.popleft()