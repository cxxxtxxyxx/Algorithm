import sys

input = sys.stdin.readline


color_papers = [list(map(int, input().split())) for __ in range(10)]

paper_count = [0] + [5] * 5

result = sys.maxsize

def check_cover(x, y, k):
    for i in range(x, x + k):
        for j in range(y, y + k):
            if color_papers[i][j] != 1:
                return False

    return True

def backtracking(x, y):

    global result

    if y == 10:
        x += 1
        y = 0

    if x == 10 and y == 0:
        result = min(result, 25 - sum(paper_count))
        return
    

    if color_papers[x][y] == 1:
        for k in range(1, 6):
            if x + k - 1 >= 10 or y + k - 1 >= 10:
                continue
            
            if paper_count[k] == 0:
                continue

            if check_cover(x, y, k):
                paper_count[k] -= 1
                for i in range(x, x + k):
                    for j in range(y, y + k):
                        color_papers[i][j] = -1
                backtracking(x, y + 1)
                paper_count[k] += 1
                for i in range(x, x + k):
                    for j in range(y, y + k):
                        color_papers[i][j] = 1
    else:
        backtracking(x, y + 1)

backtracking(0, 0)

if result == sys.maxsize:
    print(-1)
else:
    print(result)