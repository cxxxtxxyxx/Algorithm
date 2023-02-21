import sys

input = sys.stdin.readline

def recur(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    
    elif idx % 2 == 0:
        return recur(idx // 2)
    
    else:
        return 1 - recur(idx // 2)
    


k = int(input())
print(recur(k - 1))