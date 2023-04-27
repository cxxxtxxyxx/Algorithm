import sys

input = sys.stdin.readline;

N, M = map(int, input().split())

arr = list(map(int, input().split()))
prefix_sum = [0]
sum_val = 0

for i in arr:
  sum_val += i
  prefix_sum.append(sum_val)

for i in range(M):
  x, y = map(int, input().split()) 
  print(prefix_sum[y] - prefix_sum[x - 1])