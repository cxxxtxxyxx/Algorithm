def factorials(n):
  if n == 1 or n == 0:
    return 1
  return n * factorials(n - 1)

n = int(input())
result = list(str(factorials(n)))
cnt = 0



for i in range(len(result) - 1, 1, -1):
  if result[i] == '0':
    cnt += 1
  else:
    break

print(cnt)