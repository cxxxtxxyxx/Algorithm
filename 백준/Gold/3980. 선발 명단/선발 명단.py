import sys

input = sys.stdin.readline

C = int(input().strip())


def backtracking(idx, _sum):

    global result

    if idx == 11:
        result = max(_sum, result)
        return
    
    for i in range(11):
        if position[i] == False and graph[idx][i] != 0:
            position[i] = True
            backtracking(idx + 1, _sum + graph[idx][i])
            position[i] = False

for _ in range(C):
    graph = [list(map(int, input().split())) for __ in range(11)]

    result = 0
    position = [False] * 11

    backtracking(0, 0)

    print(result)