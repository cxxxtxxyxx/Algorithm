import sys
from itertools import combinations

test = list(map(int, sys.stdin.readline().split()))
while len(test) != 1:
  test = test[1:]
  if len(test) == 1:
    break
  result = list(combinations(test, 6))
  for item in result:
    print(*item)
  print()
  test = list(map(int, sys.stdin.readline().split()))