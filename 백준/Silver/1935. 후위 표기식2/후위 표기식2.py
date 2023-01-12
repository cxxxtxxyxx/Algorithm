import sys

input = sys.stdin.readline

def calc(a, b, operator):
    PLUS = "+"
    MINUS = "-"
    DIV = "/"
    MULTI = "*"

    if operator == PLUS:
        return (a + b) / 1
    elif operator == MINUS:
        return (a - b) / 1
    elif operator == MULTI:
        return (a * b) / 1
    else:
        return a / b


n = int(input())
ops = ["+", "-", "/", "*"]

formular = list(input().strip())
_num = [int(input().strip()) for _ in range(n)]

stack = []

for idx in range(len(formular)):
    if formular[idx] in ops:
        b = stack.pop()
        a = stack.pop()
        stack.append(calc(a, b, formular[idx]))
    else:
        stack.append(_num[ord(formular[idx]) - ord("A")])


print(f'{stack[0]:.2f}')