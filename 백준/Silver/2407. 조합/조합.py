import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))



def factorial(num, goal):
    if num == goal:
        return goal
    return num * factorial(num - 1, goal)

print(factorial(n, n - m + 1) // factorial(m, 1))