n = int(input())

nums = list(map(int, input().split(' ')))

cnt = n
for item in nums:
  if item == 1:
    cnt -= 1
    continue
  if item % 2 != 0:
    for i in range(2, item):
      if item % i == 0:
        cnt -= 1
        break
  else:
    if item != 2:
      cnt -= 1
      continue

print(cnt)