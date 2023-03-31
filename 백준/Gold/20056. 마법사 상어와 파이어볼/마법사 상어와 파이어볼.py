import sys
from collections import deque

input = sys.stdin.readline

"""
r, c -> i, j
질량 m
방향 d
속력 s

그래프 각 원소를 deque로 만듦
1. 모든 파이어볼 이동명령 시
해당 방향(d로) 속력 s 만큼 이동 (이동 중에는 같은 칸에 여러 파이어볼 있을 수 있음) 순회 전 미리 좌표 체크해서 여러개 있을 시 없을때까지 모두 이동시키기 / 그게 아니라면 이동시 q.popleft()로 꺼내서 이동 후 q.append로 맨 뒤에 삽입
1-1. 이동 시 범위 벗어나면 -> N + 1 -> 1, 0 -> N
2. 이동 끝난 뒤 2개 이상 파이어볼 칸에서는 다음과 같은 일
2-1. 같은 칸에 있는 파이어볼 모두 하나로 합쳐짐
2-2. 파이어볼은 4개의 파이어볼로 나누어짐
2-3. 나누어진 파이어볼의 질량 속력 방향은 다음과 같음
2-3-1. 질량은 (합쳐진 파이어볼 질량의 합) / 5
2-3-2. 속력은 (합쳐진 파이어볼 속력의 합) / (합쳐진 파이어볼의 개수)
2-3-3. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면 방향은 순차적으로 0, 2, 4, 6이 됨, 그렇지 않으면 1, 3, 5, 7
2-3-4. 질량이 0인 파이어볼은 소멸되어 없어짐
3. 이동을 K번 명령한 후 남아있는 파이어볼 질량의 합은?

i, j, 질량, 속력, 방향
1, 1, 5, 2, 2
1, 4, 7, 1, 6

* * (5, 2, 2), (7, 1, 6) => (2, 1, 0) (2, 1, 2) (2, 1, 4) (2, 1, 6) *
* * * *
* * * *
* * * *
"""

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().strip().split())

graph = [list(deque() for __ in range(N)) for __ in range(N)]
coords = deque()

for __ in range(M):
    r, c, m, s, d = map(int, input().strip().split())
    graph[r - 1][c - 1].append((m, s, d))
    coords.append((r - 1, c - 1))



def all_odd_or_even(arr):
    res = arr[0] % 2

    for i in range(1, len(arr)):
        if arr[i] % 2 != res:
            return False
        
    return True


for __ in range(K):
    for ___ in range(len(coords)):
        r, c = coords.popleft()
        m, s, d = graph[r][c].popleft()
        nr = (r + s * dx[d]) % N
        nc = (c + s * dy[d]) % N
        graph[nr][nc].append((m, s, d))
    
    for i in range(N):
        for j in range(N):
            total = len(graph[i][j])
            
            if total >= 2:
                m, s, d = 0, 0, []
                for pm, ps, pd in graph[i][j]:
                    m += pm
                    s += ps
                    d.append(pd)
                graph[i][j] = deque()
                if all_odd_or_even(d):
                    d = [0, 2, 4, 6]
                else:
                    d = [1, 3, 5, 7]
                m //= 5
                s //= total
                if m == 0:
                    continue
                for k in range(4):
                    coords.append((i, j))
                    graph[i][j].append((m, s, d[k]))
            elif total == 1:
                coords.append((i, j))
    
ans = 0

for i in range(N):
    for j in range(N):
        if len(graph[i][j]) >= 1:
            ans += sum(g[0] for g in graph[i][j])

print(ans)
    
                