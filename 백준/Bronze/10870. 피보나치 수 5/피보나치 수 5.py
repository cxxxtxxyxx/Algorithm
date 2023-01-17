import sys

input = sys.stdin.readline

n = int(input().strip())

pibo = [0, 1]

def pibonaci(idx):
    if idx == 0:
        return 0
    if idx == 1:
        return 1
    
    return pibonaci(idx - 1) + pibonaci(idx - 2)

print(pibonaci(n))