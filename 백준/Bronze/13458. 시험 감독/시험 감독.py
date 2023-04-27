N = int(input())

test_nums = list(map(int, input().split()))

B, C = map(int, input().split())

cnt = 0
left = 0
for num in test_nums:
  left = num
  left -= B
  cnt += 1
  if left > 0:
    if left % C == 0:
      cnt += left // C
    else:
      cnt += left // C + 1

print(cnt)