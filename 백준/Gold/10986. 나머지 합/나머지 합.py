import sys
N, M = map(int, input().split())
a = list(map(int, input().split())) + [0]
cnt = [0] * M
for i in range(N):
  a[i] += a[i - 1]
  cnt[a[i] % M] += 1
res = cnt[0]
for v in cnt:
  res += v * (v - 1) // 2
print(res)