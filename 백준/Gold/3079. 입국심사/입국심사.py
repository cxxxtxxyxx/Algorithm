import sys

input = sys.stdin.readline

N, M = map(int, input().split())

T = [int(input()) for __ in range(N)]

T.sort()

def binary_search():
    res = 0
    start = 1
    end = T[-1] * M
    
    while start <= end:
        count = 0
        mid = (start + end) // 2

        for el in T:
            count += mid // el

        if count >= M:
            res = mid
            end = mid - 1

        else:
            start = mid + 1

    return res

print(binary_search())
