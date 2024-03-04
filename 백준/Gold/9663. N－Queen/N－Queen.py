import sys

input = sys.stdin.readline

N = int(input())

result = 0
rows = [0] * N
def backtracking(row_idx):

    global result

    if row_idx == N:
        result += 1
        return


    
    for i in range(N):
        
        rows[row_idx] = i

        if isValid(row_idx):
            backtracking(row_idx + 1)

def isValid(row_idx):

    for i in range(row_idx):
        if rows[row_idx] == rows[i] or abs(rows[row_idx] - rows[i]) == abs(row_idx - i):
            return False
        
    return True

backtracking(0)
print(result)