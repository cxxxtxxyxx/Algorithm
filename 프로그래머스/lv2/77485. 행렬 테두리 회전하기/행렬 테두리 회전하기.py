from collections import deque

def solution(rows, columns, queries):
    answer = []

    cnt = 1
    graph = [[0] * columns for __ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = cnt
            cnt += 1

    for query in queries:
        x1, y1, x2, y2 = query

        coords = []


        q = deque()

        for j in range(y1 - 1, y2):
            coords.append((x1-1,j))
            q.append(graph[x1 - 1][j])

        for j in range(x1, x2 - 1):
            coords.append((j, y2-1))
            q.append(graph[j][y2 - 1])

        for j in range(y2 - 1, y1 - 2, - 1):
            coords.append((x2-1, j))
            q.append(graph[x2 - 1][j])

        for j in range(x2 - 2, x1 - 1, -1):
            coords.append((j, y1-1))
            q.append(graph[j][y1 - 1])

        answer.append(min(list(q)))

        q.rotate(1)
        
        for coord in coords:
            x, y = coord
            val = q.popleft()

            graph[x][y] = val 
    


    return answer


# query = x1, y1, x2, y2
# result = [8, 10, 25]
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))

# result = [1, 1, 5, 3]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))

# result = [1]
print(solution(100, 97, [[1,1,100,97]]))
