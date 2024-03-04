import sys

input = sys.stdin.readline

N = int(input().strip())

eggs = [list(map(int, input().split())) for __ in range(N)]

broken_egg_count = 0

def backtracking(idx):
    global broken_egg_count

    if idx == N:
        cnt = 0
        for idx, egg in enumerate(eggs):
            if egg[0] <= 0:
                cnt += 1
        
        broken_egg_count = max(broken_egg_count, cnt)
        return
    
    if eggs[idx][0] <= 0:
        backtracking(idx + 1)
        return
    
    for i in range(N):
        if i != idx and eggs[i][0] > 0:
            break
    else:
        broken_egg_count = max(N - 1, broken_egg_count)
        return 
    
    for i in range(N):
        if i == idx or eggs[i][0] <= 0:
            continue

        eggs[i][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]
        backtracking(idx + 1)
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]


backtracking(0)
print(broken_egg_count)