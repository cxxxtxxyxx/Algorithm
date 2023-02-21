import sys

input = sys.stdin.readline

N = int(input())

matrix = [list(map(int, input().split())) for __ in range(N)]

def divide_conquer(N, x, y):

    divide = N // 2

    if divide == 1:
        answer = [matrix[x][y], matrix[x + 1][y], matrix[x][y + 1], matrix[x + 1][y + 1]]
        answer.sort()
        return answer[-2]
    
    a = divide_conquer(divide, x, y)
    b = divide_conquer(divide, x + divide, y)
    c = divide_conquer(divide, x, y + divide)
    d = divide_conquer(divide, x + divide, y + divide)

    res = [a, b, c, d]
    res.sort()

    return res[-2]


print(divide_conquer(N, 0, 0))