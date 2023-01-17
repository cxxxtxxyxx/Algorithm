import sys
import copy
import itertools

input = sys.stdin.readline

n = int(input().strip())

paper = [list(input().split()) for __ in range(n)]
white_cnt = 0
blue_cnt = 0

def getPaper(paper, n):
    global white_cnt
    global blue_cnt

    if n == 1:
        if paper[0][0] == '0':
            
            white_cnt += 1
        else:
            blue_cnt += 1
        return

    a = copy.deepcopy(paper[:n // 2])
    c = copy.deepcopy(paper[n // 2:])

    b = []
    d = []
    for i in range(n // 2):
        b.append(copy.deepcopy(a[i][n // 2:]))
        d.append(copy.deepcopy(c[i][n // 2:]))
        a[i] = a[i][: n // 2]
        c[i] = c[i][: n // 2]

    del_dupl_a = set(list(itertools.chain(*a)))
    del_dupl_b = set(list(itertools.chain(*b)))
    del_dupl_c = set(list(itertools.chain(*c)))
    del_dupl_d = set(list(itertools.chain(*d)))

    

    if len(del_dupl_a) == 1:
        if list(del_dupl_a)[0] == '0':
            white_cnt += 1
        else:
            blue_cnt += 1
    else:
        getPaper(a, n // 2)

    if len(del_dupl_b) == 1:
        if list(del_dupl_b)[0] == '0':
            white_cnt += 1
        else:
            blue_cnt += 1
    else:
        getPaper(b, n // 2)
    
    if len(del_dupl_c) == 1:
        if list(del_dupl_c)[0] == '0':
            white_cnt += 1
        else:
            blue_cnt += 1
    else:
        getPaper(c, n // 2)
    
    if len(del_dupl_d) == 1:
        if list(del_dupl_d)[0] == '0':
            white_cnt += 1
        else:
            blue_cnt += 1
    else:
        getPaper(d, n // 2)

if len(set(list(itertools.chain(*paper)))) == 1:
    if list(set(list(itertools.chain(*paper))))[0] == "0":
        print(1)
        print(0)
    else:
        print(0)
        print(1)
    exit()

getPaper(paper, n)
print(white_cnt)
print(blue_cnt)