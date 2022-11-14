import sys

"""
총 커서 위치 => 길이 L 기준 L + 1
L 커서를 왼쪽으로 한칸 옮김 (문장 맨 앞이면 무시)
R 커서를 오른쪽으로 한칸 옮김 (문장 맨 뒤면 무시)
B 커서 왼쪽 문자를 지움(문장 맨 앞이면 무시) (커서 위치 그대로)
P $ $문자를 커서 왼쪽에 추가함
"""

# testCase = list(input().replace('\n', ''))
# cursor = len(testCase)
# n = int(input())
# for i in range(n):
#   app = sys.stdin.readline().replace('\n', '').split(' ')
  
#   if app[0] == 'L':
#     if cursor != 0:
#       cursor -= 1

    
#   elif app[0] == 'D':
#     if cursor != len(testCase):
#       cursor += 1

    
#   elif app[0] == 'B':
#     if cursor != 0:
#       if cursor == len(testCase):
#         del testCase[cursor - 1]
#         cursor = len(testCase)

#       else:
#         del testCase[cursor - 1]
#         cursor -= 1

    
    
#   else:
#     testCase.insert(cursor, app[1])
#     cursor += 1

# print(''.join(testCase))

#-------------------------

# 커서를 기준으로 양쪽을 스택으로 분해
# 마지막에 다시 합치기

st1 = list(input().replace('\n', ''))
st2 = []
n = int(input())
for i in range(n):
  app = sys.stdin.readline().replace('\n', '').split(' ')
  if app[0] == 'L':
    if st1:
      st2.append(st1.pop())
  
  elif app[0] == 'D':
    if st2:
      st1.append(st2.pop())
  
  elif app[0] == 'B':
    if st1:
      st1.pop()
  
  else:
    st1.append(app[1])
    

st1.extend(reversed(st2))
print(''.join(st1))