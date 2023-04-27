N, M = map(int, input().split())
DNA = []

result = ''
cnt = 0

for i in range(N):
  DNAs = list(input())
  DNA.append(DNAs)
  
for i in range(M):
  a, c, g, t = 0, 0, 0, 0
  for j in range(N):
    if DNA[j][i] == 'A':
      a += 1
    elif DNA[j][i] == 'C':
      c += 1
    elif DNA[j][i] == 'G':
      g += 1
    else:
      t += 1
  if max(a, c, g, t) == a:
    result += 'A'
    cnt += c + g + t
  elif max(a, c, g, t) == c:
    result += 'C'
    cnt += a + g + t
  elif max(a, c, g, t) == g:
    result += 'G'
    cnt += a + c + t
  else:
    result += 'T'
    cnt += a + c + g

print(result)
print(cnt)

