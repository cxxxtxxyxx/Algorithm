import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
stack = []

def getSolution():
    if len(stack) == m:
        print(*stack)
        return

    for i in range(1, n + 1):
        if not i in stack:
            if len(stack) != 0:
                if stack[len(stack) - 1] < i:
                    stack.append(i)
                    getSolution()
                    stack.pop()
            else:
                stack.append(i)
                getSolution()
                stack.pop()

getSolution()