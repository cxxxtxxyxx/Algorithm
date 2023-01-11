import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    op = input().split()

    if op[0] == "push":
        stack.append(int(op[1]))

    elif op[0] == "pop":
        if len(stack) == 0:
            print(-1)
            continue

        print(stack.pop())

    elif op[0] == "size":
        print(len(stack))
    
    elif op[0] == "empty":
        if len(stack) == 0:
            print(1)
            continue
        print(0)
    else:
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])