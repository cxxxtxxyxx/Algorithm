from collections import deque

infix = list(input())
postfix = deque()


stack = deque()

op_val = {
  '(' : 0,
  '+' : 1,
  '-' : 1,
  '*' : 2,
  '/' : 2
}

for item in infix:
  if 'A' <= item and item <= 'Z':
    print(item, end="")
  else:
    if not stack:
      stack.append(item)
    else:
      if item == '(':
        stack.append(item)
      elif item == ')':
        size = len(stack)
        while stack and stack[size - 1] != '(':
          print(stack.pop(), end="")
          size = len(stack)
        stack.pop()
      else:
        size = len(stack)
        if stack and op_val[item] <= op_val[stack[size - 1]]:
          size = len(stack)
          while stack and op_val[item] <= op_val[stack[size - 1]]:
            print(stack.pop(), end="")
            size = len(stack)
          stack.append(item)
        else:
          stack.append(item)
while(stack):
  print(stack.pop(), end="")