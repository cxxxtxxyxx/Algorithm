import sys

def dfsR(i, j):
  if i < 0 or i > N - 1 or j < 0 or j > N - 1 or graph[i][j] == 0:
    return 0
  
  if visited[i][j] == False and graph[i][j] == 1:
    visited[i][j] = True
    total = 1
    total += dfsR(i - 1, j)
    total += dfsR(i + 1, j)
    total += dfsR(i, j - 1)
    total += dfsR(i, j + 1)
    return total
  return 0

N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
result = []
for _ in range(N):
  apart = list(map(int, list(sys.stdin.readline().rstrip())))
  graph.append(apart)

for i in range(N):
  for j in range(N):
    sum_ = dfsR(i, j)
    if sum_ != 0:
      result.append(sum_)

result.sort()
print(len(result), *result)
      
