import sys

input = sys.stdin.readline

def hanoi(start, sub, end, idx):
    if idx >= 1:
        hanoi(start, end, sub, idx - 1)
        print(start, end)
        hanoi(sub, start, end, idx - 1)


n = int(input())

print(2 ** n - 1)

hanoi(1, 2, 3, n)