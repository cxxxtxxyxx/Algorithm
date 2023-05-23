import sys
import heapq

INF = sys.maxsize


def solution(N, road, K):
    answer = 0
    graph = [[] for __ in range(N + 1)]
    
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
    distance = [INF] * (N + 1)
    dijkstra(1, distance, graph)
    
    return len(list(filter(lambda x: x <= K, distance)))

def dijkstra(start, distance, graph):
    heap = []
    distance[start] = 0
    
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
            
        for node in graph[now]:
            cost = dist + node[1]
            
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(heap, (cost, node[0]))
    
    
    