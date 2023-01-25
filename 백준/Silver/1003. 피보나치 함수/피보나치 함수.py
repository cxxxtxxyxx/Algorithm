import sys

input = sys.stdin.readline

n = int(input())

zero_count = [1, 0, 1] + [0] * 38
one_count = [0, 1, 1] + [0] * 38

for i in range(3, 41):
    zero_count[i] = zero_count[i - 1] + zero_count[i - 2]
    one_count[i] = one_count[i - 1] + one_count[i - 2]

for __ in range(n):
    cnt = int(input())
    print(zero_count[cnt], one_count[cnt])