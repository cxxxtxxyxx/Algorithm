import sys

input = sys.stdin.readline

T = int(input())

for __ in range(T):

    N, M, K = map(int, input().split())

    homes = list(map(int, input().split()))

    start, end = 1, M - 1

    res = 0

    _sum = sum(homes[:end+1])
    if _sum < K:
        res += 1

    while start < N:

        _sum -= homes[start - 1]
        _sum += homes[(end + 1) % N]

        if _sum < K:
            res += 1

        start += 1
        end += 1

    
    if M == N:
        if res != 0:
            print(1)
        else:
            print(0)

    else:
        print(res)


