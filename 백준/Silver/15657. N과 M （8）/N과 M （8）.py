import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

nums = sorted(list(map(int, input().strip().split())))

def backtracking(tmp):
    if len(tmp) == M:
        print(*tmp)
        return
    
    for i in range(0, N):
        if len(tmp) != 0:
            if nums[i] >= tmp[-1]:
                tmp.append(nums[i])
                backtracking(tmp)
                tmp.pop()
        else:
            tmp.append(nums[i])
            backtracking(tmp)
            tmp.pop()

backtracking([])