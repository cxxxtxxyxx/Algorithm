N = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

max_ = cards[0]
result = 0

for i in range(1, N):
  result += max_ + cards[i]

print(result)
