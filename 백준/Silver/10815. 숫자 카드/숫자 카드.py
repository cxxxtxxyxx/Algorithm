import sys
from bisect import bisect_right, bisect_left

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
tests = list(map(int, input().split()))

result = []

for test in tests:
    left = bisect_left(cards, test)
    right = bisect_right(cards, test)
    if right - left == 1:
        result.append(1)

    else:
        result.append(0)

print(*result)