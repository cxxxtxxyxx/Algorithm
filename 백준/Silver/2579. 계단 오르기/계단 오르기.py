import sys

input = sys.stdin.readline

stair_cnt = int(input())

stairs = [0] + [int(input()) for __ in range(stair_cnt)]


res = [0] * (stair_cnt + 1)

res[1] = stairs[1]
if stair_cnt == 1:
    print(res[1])
    exit()
res[2] = stairs[1] + stairs[2]
if stair_cnt == 2:
    print(res[2])
    exit()
res[3] = max(stairs[1] + stairs[3], stairs[2] + stairs
[3])
if stair_cnt == 3:
    print(res[3])
    exit()

for i in range(4, stair_cnt + 1):
    res[i] = max(res[i - 3] + stairs[i - 1] + stairs[i], res[i - 2] + stairs[i])

print(res[stair_cnt])