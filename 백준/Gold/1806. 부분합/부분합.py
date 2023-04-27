N, S = map(int, input().split())

nums = list(map(int, input().split()))

if sum(nums) < S:
  print(0)
  exit()

minimum = N + 1
start = 0
end = 0
s = nums[0]
while True:
  # print(f'start = {start}, end = {end}, minimum = {minimum}')
  if s >= S:
    s -= nums[start]
    minimum = min(minimum, end - start + 1)
    start += 1
  else:
    end += 1
    if end == N:
      break
    s += nums[end]
  

print(minimum)