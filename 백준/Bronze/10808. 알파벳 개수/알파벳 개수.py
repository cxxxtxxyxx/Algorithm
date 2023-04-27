
word = input()

result = [0] * 26

for item in word:
  index = ord(item) - ord('a')
  result[index] += 1

print(*result)