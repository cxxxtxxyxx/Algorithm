import sys
N = int(input())

ropes = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
ropes.sort(reverse=True)
max_ = 0
for i in range(N):
  ropes[i] = ropes[i] * (i + 1)
  
# print(ropes)

print(max(ropes))