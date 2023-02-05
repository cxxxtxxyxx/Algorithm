# 요구사항 & 아이디어
"""
상근이네 집에서 맥주 한박스를 들고 출발
맥주 한 박스에 맥주가 20개
50m 당 한병 마심 => 50미터를 가려면 그 직전에 맥주 한병을 마셔야 함
빈병 버리고 맥주 구매 가능
맥주 20병 넘을 수 없음
편의점 나선 직후에도 50미터를 가기 전에 맥주 한 병 마셔야함

편의점, 상근이네 집, 펜타포트 좌표

테스트 케이스 개수 t (t <= 50)
각 테스트 케이스 첫째 줄 편의점 개수 n (0 <= n <= 100)

맥주 충분 => happy 출력
중간에 맥주 바닥나면 sad

==> 맥주 == 연료
연료 1통당 50m

상근이네 집 좌표 입력
편의점 좌표 입력 * n
펜타포트 좌표

max(abs) 값 + 1 ==> 0 <= 그래프 <= max 값
"""
# 자료구조 & 알고리즘
"""

"""

import sys
from collections import deque
import copy
input = sys.stdin.readline

t = int(input())

# def get_conv_cond(result):

#     if len(result) == n:
#         # print(result)
#         conv_cond.append(copy.deepcopy(result))
#         return
    
#     for i in range(len(conv)):
#         if not conv[i] in result:
#             result.append(conv[i])
#             get_conv_cond(result)
#             result.pop()


def get_dist(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def bfs(x, y):
    q = deque([(x, y)])
    
    while q:
        i, j = q.popleft()
        if get_dist(i, festival_x, j, festival_y) <= 1000:
            print("happy")
            return True
        
        for k in range(n):
            if visited[k] == False:
                con_x, con_y = conv[k]
                if get_dist(con_x, i, con_y, j) <= 1000:
                    q.append((con_x, con_y))
                    visited[k] = True
        
    print("sad")
    return False

                

for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    conv = []
    for __ in range(n):
        x, y = map(int, input().split())
        conv.append((x, y))
    festival_x, festival_y = map(int, input().split())
    # print(conv)

    # get_conv_cond([])
    visited = [False] * (n + 1)

    bfs(home_x, home_y)
    
