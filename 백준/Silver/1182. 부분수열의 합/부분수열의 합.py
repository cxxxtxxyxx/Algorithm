import sys
from itertools import combinations

input = sys.stdin.readline

n, s = list(map(int, input().split()))

input_nums = list(map(int, input().split()))
input_nums.sort()
count = 0

for i in range(1, n + 1):
    comb = list(combinations(input_nums, i))
    for items in comb:
        if sum(items) == s:
            count += 1

print(count)