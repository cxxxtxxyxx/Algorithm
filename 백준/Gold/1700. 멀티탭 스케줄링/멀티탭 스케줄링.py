N, K = map(int, input().split())

array = list(map(int, input().split()))
multi = [0] * N

res = swap = num = max_ = 0

for i in array:
  if i in multi:
    pass
  elif 0 in multi:
    multi[multi.index(0)] = i
  else:
    for j in multi:
      if j not in array[num:]:
        swap = j
        break
      elif array[num:].index(j) > max_:
        max_ = array[num:].index(j)
        swap = j
    multi[multi.index(swap)] = i
    max_ = swap = 0
    res += 1

  num += 1

print(res)