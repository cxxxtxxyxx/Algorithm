import sys

input = sys.stdin.readline

n = int(input())

_OPEN = "("
_CLOSE = ")"
_YES = "YES"
_NO = "NO"

for _ in range(n) :
    parenthesis = list(input().strip())
    stack = []
    result = _YES
    for el in parenthesis:
        if el == _OPEN:
            stack.append(el)

        else:
            if len(stack) == 0:
                result = _NO
                break
            else:
                stack.pop()

    if len(stack) != 0:
        result = _NO
    else:
        if result != _NO:
            result = _YES
    print(result)