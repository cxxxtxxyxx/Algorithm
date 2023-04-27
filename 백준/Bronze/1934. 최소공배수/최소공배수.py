def maximum(a, b):
  if a == b:
    return a
  elif a > b:
    big = a
  else:
    big = b
  max_num = 0
  for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
      max_num = i
  return max_num

n = int(input())

for _ in range(n):
  a, b = map(int, input().split(' '))
  c = maximum(a, b)
  print(a * b // c)
