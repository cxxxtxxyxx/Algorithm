import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline



N, M = map(int, input().split())

styles = []
powers = []
for __ in range(N):
    style, power = input().split()
    power = int(power)
    styles.append(style)
    powers.append(power)

character_powers = [int(input()) for __ in range(M)]

res = []

for power in character_powers:
    idx = bisect_left(powers, power)
    res.append(styles[idx])

for el in res:
    print(el)