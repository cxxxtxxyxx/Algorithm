# 아이디어
"""

"""

# 시간복잡도
"""

"""

# 자료구조
"""
그래프 사용
"""


import sys

input = sys.stdin.readline

t = int(input())


def dfs(v, visited):
    visited[v] = True

    for node in graph[v]:
        if visited[node] == False:
            dfs(node, visited)

    return 1


for __ in range(t):
    n = int(input())
    edge = [0] + list(map(int, input().split()))

    graph = [[0] * (n + 1) for __ in range(n + 1)]

    for i, j in enumerate(edge):
        if i != j:
            graph[i].append(j)
            graph[j].append(i)
        else:
            graph[i].append(j)
            
    visited = [False] * (n + 1)
    visited[0] = True
    result = 0
    while not all(visited):
        v = visited.index(False)
        result += dfs(v, visited)

    print(result)


