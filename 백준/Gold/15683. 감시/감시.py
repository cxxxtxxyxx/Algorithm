# 1번 한 방향
# 2번 직선으로 두 방향
# 3번 직각으로 두 방향
# 4번 세 방향
# 5번 네 방향
# 6번 벽
"""
벽은 통과 불가
CCTV는 통과 가능
"""

import copy
import sys
from itertools import chain

input = sys.stdin.readline

N, M = map(int, input().split())

cctv = [list(map(int, input().split())) for __ in range(N)]
cctvs = []
answer = 1e9
for i in range(N):
    for j in range(M):
        if cctv[i][j] in [1, 2, 3, 4, 5]:
            cctvs.append((i, j, cctv[i][j]))

# 동 남 서 북 (시계방향)
# 1번 동남북서
# 2번 가로 세로
# 3번 북동 동남 남서 북서
# 4번 동남북 남동서 서남북 북동서
# 5번 모두 똑같음
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
idx = [0, 1, 2, 3]

cctv_dicrection = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 3], [0, 1], [1, 2], [2, 3]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]]
}

def dfs(cctv, depth):
    global answer

    if depth == len(cctvs):
        answer = min(answer, len(list(filter(lambda x: x == 0, list(chain(*cctv))))))
        return
    
    
    copy_cctv = copy.deepcopy(cctv)

    x, y, cctv_number = cctvs[depth]

    for direction in cctv_dicrection[cctv_number]:
        check(x, y, direction, copy_cctv)
        dfs(copy_cctv, depth + 1)
        copy_cctv = copy.deepcopy(cctv)

def check(x, y, direction, cctv):
    for direct in direction:

        nx = x
        ny = y

        while True:
            nx += dx[direct]
            ny += dy[direct]

            if not (0 <= nx < N and 0 <= ny < M):
                break

            if cctv[nx][ny] == 6:
                break

            if cctv[nx][ny] == 0:
                cctv[nx][ny] = -1


dfs(cctv, 0)
print(answer)