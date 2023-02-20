import sys
from collections import deque
input = sys.stdin.readline

def is_move_valid(nx, ny, x, y):
    return abs(nx - x) <= 2 and abs(ny - y) <= 2

n, T = map(int, input().split())

hole = set()

for __ in range(n):
    hole.add(tuple(map(int, input().split())))

# hole.sort(key=lambda x: (x[0], x[1]))


visited = [False] * n

# def binary_search(cx, cy):

#     start = 0
#     end = n - 1

#     res = []
#     while start <= end:
#         mid = (start + end) // 2

#         if is_move_valid(cx, cy, hole[mid][0], hole[mid][1]):
#             visited[mid] = True
#             res.append((hole[mid][0], hole[mid][1], mid))
#             start = mid + 1
#         else:
#             end = mid - 1

#     return res

def bfs():
    q = deque()
    q.append([0, 0, 0])
    while q:
        cx, cy, cnt = q.popleft()
        if cy == T:
            return cnt

        for i in range(-2, 3):
            for j in range(-2, 3):
                nx = cx + i
                ny = cy + j
                if (nx, ny) in hole:
                    q.append([nx, ny, cnt + 1])
                    hole.remove((nx, ny))
        # for i in range(0, n - 1):
        #     print(hole[i][0], hole[i][1])
        #     if visited[i] == False and is_move_valid(hole[i][0], hole[i][1], cx, cy):
        #         q.append((hole[i][0], hole[i][1], i))
        #         visited[i] = True

    return -1

# candidate_hole = binary_search(0, 0)
print(bfs())



