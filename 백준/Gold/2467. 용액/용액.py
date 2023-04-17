import sys

input = sys.stdin.readline

N = int(input())

liquid = list(map(int, input().split()))

liquid.sort()


if liquid[-1] < 0:
    print(liquid[-2], liquid[-1])
    exit()

if liquid[0] > 0:
    print(liquid[0], liquid[1])
    exit()


start, end = 0, N - 1

idx_res = [liquid[start], liquid[end]]

_min = liquid[start] + liquid[end]

while start < end:

    _sum = liquid[start] + liquid[end]

    if abs(_sum) < abs(_min):
        idx_res = [liquid[start], liquid[end]]
        
        _min = abs(_sum)

        if _min == 0:
            break


    if _sum < 0:
        start += 1

    else:
        end -= 1


print(*idx_res)