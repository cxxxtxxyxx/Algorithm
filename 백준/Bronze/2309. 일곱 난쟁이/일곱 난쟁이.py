import sys
from itertools import combinations

idx = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8], 2))

cnt = 0
test = []

for _ in range(9):
  test.append(int(sys.stdin.readline().strip()))
while True:
  result = []
  for i in range(9):
    if i != idx[cnt][0] and i != idx[cnt][1]:
      result.append(test[i])
  if sum(result) == 100:
    result = sorted(result)
    for i in range(7):
      print(result[i])
    break
  cnt += 1

