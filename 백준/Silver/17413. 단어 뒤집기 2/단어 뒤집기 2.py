import sys
import re

testCase = sys.stdin.readline().strip()

p = re.compile('<[0-9a-zA-Z ]+>|[0-9a-zA-Z ]')
objs = p.findall(testCase)
stack = []
result = ''

for obj in objs:
  if obj[0] == '<':
    while stack:
      result += stack.pop()
    result += obj
  elif obj == ' ':
    while stack:
      result += stack.pop()
    result += ' '
  else:
    stack.append(obj)

while stack:
  result += stack.pop()

print(result)