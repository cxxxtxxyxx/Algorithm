from collections import deque

"""
3 2 7 2 
4 6 5 1
14, 16
---
3 2 7 2 4
6 5 1
18, 12
---
2 7 2 4
6 5 1 3
15, 15
"""

def solution(queue1, queue2):
    answer = -2
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(q1), sum(q2)
    cnt = 0
    size = len(queue1)
    
    if q1_sum == q2_sum:
        return 0
    while True:
        if cnt >= size * 3:
            return -1
        if q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
            cnt += 1
        elif q1_sum == q2_sum:
            return cnt
        else:
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num
            cnt += 1