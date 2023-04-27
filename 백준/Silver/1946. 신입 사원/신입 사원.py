import sys
T = int(input())

for _ in range(T):
  N = int(sys.stdin.readline().rstrip())
  ap = []
  cnt = 1
  for i in range(N):
    ap.append(list(map(int, sys.stdin.readline().rstrip().split())))
  
  ap.sort()
  
  max_ = ap[0][1]
  for i in range(1, N):
    if max_ > ap[i][1]:
      cnt += 1
      max_ = ap[i][1]


  print(cnt)