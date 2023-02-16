"""
산성용액 1 ~ 1_000_000_000
알칼리성 -1_000_000_000 ~ -1
"""


import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())

solutions = list(map(int, input().split()))
solutions.sort()
res = []

if solutions[-1] < 0:
    print(solutions[-2], solutions[-1])
    exit(0)

if solutions[0] > 0:
    print(solutions[0], solutions[1])
    exit(0)    
_min = sys.maxsize

# negative_start = 0
# positive_start = bisect_left(solutions, 0)
# negative_end = positive_start - 1
# positive_end = n - 1

for i in range(n - 1):

    start = i + 1
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if abs(solutions[i] + solutions[mid]) <= _min:
            res.append((solutions[i], solutions[mid]))
            _min = abs(solutions[i] + solutions[mid])
            if solutions[i] + solutions[mid] < 0:
                start = mid + 1

            else:
                end = mid - 1
        else:
            if solutions[i] + solutions[mid] < 0:
                start = mid + 1

            else:
                end = mid - 1

print(res[-1][0], res[-1][1])