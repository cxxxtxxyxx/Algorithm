# 시간초과
# import sys

# test_case = input().replace('()', '!')

# stack = []
# result = 0
# laser_count = 0

# for item in test_case:
#   if item == ')':
#     while True:
#       laser = stack.pop()
#       if laser == '!':
#         laser_count += 1
#       else:
#         break
#     result += laser_count + 1
#     for _ in range(laser_count):
#       stack.append('!')
#     laser_count = 0
#   else:
#     stack.append(item)
  

# print(result)

import sys

test_case = input()

stack = []
result = 0
start = 0

for i in range(len(test_case)):
  if test_case[i] == '(':
    start += 1
  else:
    if test_case[i - 1] == '(':
      start -= 1
      result += start
    else:
      result += 1
      start -= 1

print(result)