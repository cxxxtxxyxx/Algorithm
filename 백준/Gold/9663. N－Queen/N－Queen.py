import sys

input = sys.stdin.readline

n = int(input())
rows = [0] * n

def is_valid(v):
    for i in range(v):
        if rows[i] == rows[v] or abs(rows[i] - rows[v]) == abs(v - i):
            return False
    return True

count = 0
def dfs(v):
    global count
    if v == n:
        count += 1
        return
    
    for i in range(n):
        rows[v] = i
        if is_valid(v):
            dfs(v + 1)
            


dfs(0)
print(count)
