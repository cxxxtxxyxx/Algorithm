import sys

input = sys.stdin.readline

n = int(input())

res = [0] * 1000001

res[1] = 0
res[2] = 1
res[3] = 1
res[4] = 2

for i in range(5, 1000001):
    _min = 0
    if i % 3 == 0 and i % 2 == 0:
        _min = min(res[i // 3], res[i // 2], res[i - 1])
        if _min == res[i // 3]:
            res[i] = 1 + res[i // 3]
        elif _min == res[i // 2]:
            res[i] = 1 + res[i // 2]
        else:
            res[i] = 1 + res[i - 1]
    elif i % 3 == 0 and i % 2 != 0:
        _min = min(res[i // 3], res[i - 1])
        if _min == res[i // 3]:
            res[i] = 1 + res[i // 3]
        else:
            res[i] = 1 + res[i - 1]
    elif i % 2 == 0 and i % 3 != 0:
        _min = min(res[i // 2], res[i - 1])
        if _min == res[i // 2]:
            res[i] = 1 + res[i // 2]
        else:
            res[i] = 1 + res[i - 1]
    else:
        res[i] = 1 + res[i - 1]


print(res[n])