import sys
from collections import deque

n = int(input())
testCase = list(map(int, sys.stdin.readline().strip().split(' ')))

result = [-1] * n
stack = deque()

for i in range(n):
  while stack and (stack[-1][0] < testCase[i]):
    num, idx = stack.pop()
    result[idx] = testCase[i]
  stack.append([testCase[i], i])

for item in result:
  print(item, end=" ")

