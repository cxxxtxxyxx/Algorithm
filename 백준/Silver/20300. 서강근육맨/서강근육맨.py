import sys

input = sys.stdin.readline

N = int(input())

mus = list(map(int, input().split()))

mus.sort()


_max = 0

if N % 2 == 0:
    for i in range(len(mus) // 2):
        _max = max(_max, mus[i] + mus[N - 1 - i])
    print(_max)

else:
    for i in range(len(mus) // 2):
        _max = max(_max, mus[i] + mus[N - 2 - i])
    print(max(_max, mus[N - 1]))
