import sys
import copy
from collections import deque



def bfs(n, info):
    q = deque([(0, [0,0,0,0,0,0,0,0,0,0,0])])
    _max = -1
    result = []
    while q:
        focus, arrow = q.popleft()

        if sum(arrow) == n:
            lion, apeach = 0, 0

            for i in range(len(arrow)):
                if arrow[i] == 0 and info[i] == 0:
                    continue
                if arrow[i] > info[i]:
                    lion += 10 - i
                else:
                    apeach += 10 - i
            if lion > apeach:
                if _max < lion - apeach:
                    _max = lion - apeach
                    result.clear()
                    result.append(arrow)

                elif _max == lion - apeach:

                    result.append(arrow)
                else:
                    continue
        elif sum(arrow) > n:
            continue
        elif focus == 10:
            tmp = copy.deepcopy(arrow)
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
            
        
        else:
            tmp = copy.deepcopy(arrow)
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))
            # print(tmp)

            tmp2 = copy.deepcopy(arrow)
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))
            # print(tmp2)

    return result


def solution(n, info):
    final = bfs(n, info)
    # print(final)
    # print(final)
    if len(final) == 0:
        return [-1]
    elif len(final) == 1:
        return final[0]
    else:
        return final[-1]