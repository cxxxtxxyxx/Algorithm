import sys
from collections import deque;

n = int(input())
Deque = deque()

for _ in range(n):
  testCase = sys.stdin.readline().strip().split(' ')
  command = testCase[0]
  
  if command == 'push_front':
    n = int(testCase[1])
    Deque.appendleft(n)
  elif command == 'push_back':
    n = int(testCase[1])
    Deque.append(n)
  elif command == 'pop_front':
    if len(Deque) != 0:
      print(Deque.popleft())
    else:
      print(-1)
  elif command == 'pop_back':
    if len(Deque) != 0:
      print(Deque.pop())
    else:
      print(-1)

  elif command == 'size':
    print(len(Deque))

  elif command == 'empty':
    if len(Deque) == 0:
      print(1)
    else:
      print(0)
  elif command == 'front':
    if len(Deque) != 0:
      print(Deque[0])
    else:
      print(-1)

  else:
    if len(Deque) != 0:
      print(Deque[len(Deque) - 1])
    else:
      print(-1)

