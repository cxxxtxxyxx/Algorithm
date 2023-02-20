import sys

input = sys.stdin.readline

N = int(input())

sol = list(map(int, input().split()))

sol.sort()

if sol[0] > 0:
    print(sol[0], sol[1], sol[2])
    exit(0)

if sol[-1] < 0:
    print(sol[-3], sol[-2], sol[-1])
    exit(0)

"""
-97 -6 -2 6 98
"""
"""
이분탐색 2번
=> 음수 1개 양수 2개
=> 양수 1개 음수 2개
"""
res = []
_min = sys.maxsize
for i in range(N - 2):
    start = i + 1
    end = N - 1

    while start < end:

        if abs(sol[i] + sol[start] + sol[end]) < _min:
            _min = abs(sol[i] + sol[start] + sol[end])
            res.append((sol[i], sol[start], sol[end]))

        
        if sol[i] + sol[start] + sol[end] < 0:
            start += 1
        else:
            end -= 1

print(*res[-1])