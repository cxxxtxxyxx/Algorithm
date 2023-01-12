import sys

input = sys.stdin.readline


k = int(input())

stack = []

for __ in range(k):
    _num = input().strip()

    if _num == "0":
        stack.pop()
    else:
        stack.append(int(_num))
        
print(sum(stack))