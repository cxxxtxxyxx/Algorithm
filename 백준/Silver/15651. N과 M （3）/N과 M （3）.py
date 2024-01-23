import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())


def backtracking(tmp):
    if len(tmp) == M:
        print(*tmp)
        return
    
    for i in range(1, N + 1):
        tmp.append(i)
        backtracking(tmp)
        tmp.pop()


backtracking([])
