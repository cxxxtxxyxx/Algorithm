import sys

input = sys.stdin.readline


n = int(input())


stack = []

def getSequence():
    if len(stack) == n:
        print(*stack)

    for i in range(1, n + 1):
        if not i in stack:
            stack.append(i)
            getSequence()
            stack.pop()

getSequence()