# import sys
# input = sys.stdin.readline

# L, C = input().split()
# words = input().split()
# words.sort()

# vow_dict = ['a', 'e', 'i', 'o', 'u']

# vow_c = 0
# vow = 0

# def backtracking(idx, word):
#   if idx >= C or len(word) >= L:
#     return
  
#   if vow >= 1 and vow_c >= 2:
#     word += words[idx]
#     backtracking(idx + 1, word.replace(words[idx]))
#     backtracking(idx + 1, word)
    
  
  


import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
words = input().split()
words.sort()

vow_dict = ['a', 'e', 'i', 'o', 'u']
vow = 0
vow_c = 0

per = list(combinations(words, L))

for item in per:
  vow = 0
  vow_c = 0
  for voc in filter(lambda x: x in vow_dict, item):
    vow += 1
  vow_c = L - vow
  if vow >= 1 and vow_c >= 2:
    for i in item:
      print(i, end="")
    print()
    