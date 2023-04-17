import sys

input = sys.stdin.readline

T = int(input())

for __ in range(T):

    N, M, K = map(int, input().strip().split())

    home = list(map(int, input().strip().split()))

    res = 0

    start, end = 0, M - 1
    prev = 0
    _sum = sum(home[start:end + 1])

    if M == N:
        if sum(home) < K:
            print(1)
        else:
            print(0)

        continue

    while start < N:

        prev = home[start]

        start += 1
        end += 1

        _sum -= prev
        _sum += home[end % N]

        if _sum < K:
            res += 1

        

    print(res)