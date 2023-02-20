"""
1 2 3
2 4 6
3 6 9

"""

import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

def binary_search():

    start = 1
    end = k

    answer = 0
    while start <= end:
        cnt = 0

        mid = (start + end) // 2

        for i in range(1, N + 1):
            cnt += min(mid // i, N)

        
        if cnt < k:
            start = mid + 1

        else:
            answer = mid
            end = mid - 1


    return answer

print(binary_search())