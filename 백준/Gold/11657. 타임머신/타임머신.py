import sys

INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for __ in range(M)]

def bellman_ford(start):
    distance[start] = 0

    for i in range(N):
        for j in range(M):
            current, next, cost = graph[j]
            current -= 1
            next -= 1

            if distance[current] != INF and distance[next] > distance[current] + cost:
                distance[next] = distance[current] + cost
                if i == N - 1:
                    return True
                
    return False

distance = [INF] * N
negative_cycle = bellman_ford(0)

if negative_cycle:
    print(-1)
    exit(0)

for idx in range(1, N):
    if distance[idx] == INF:
        print(-1)
    else:
        print(distance[idx])

