import re
import sys

input = sys.stdin.readline

T = int(input().strip())

for __ in range(T):

    W = input().strip()
    K = int(input().strip())

    alpha = {}
    _min = sys.maxsize
    _max = 0

    for i in range(len(W)):
        if W[i] not in alpha:
            alpha[W[i]] = [i]
        else:
            alpha[W[i]].append(i)

    for key in alpha.keys():
        for j in range(len(alpha[key]) - (K - 1)):
            _min = min(_min, alpha[key][j + K - 1] - alpha[key][j] + 1)
            _max = max(_max, alpha[key][j + K - 1] - alpha[key][j] + 1)

    if _min == sys.maxsize and _max == 0:
        print(-1)
        continue
    
    

    print(_min, _max)
