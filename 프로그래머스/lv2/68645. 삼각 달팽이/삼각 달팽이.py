from itertools import chain
def solution(n):
    # answer = [0] * (n * (n + 1) // 2 + 1)
    answer = [[0] * i for i in range(n + 1)]
    max_num = (n * (n + 1)) // 2
    

    currentNum = 1
    startidx = 0
    startline = 1
    endline = n - 1
    size = n
    count = 1
    
    while True:
        if currentNum == max_num + 1:
            break
            
        for i in range(startline, endline + 2):
            answer[i][startidx] = currentNum
            currentNum += 1
            if currentNum == max_num + 1:
                break
        
        for i in range(startidx + 1, startidx + size):
            answer[endline+1][i] = currentNum
            currentNum += 1
            if currentNum == max_num + 1:
                break
        
        for i in range(endline, startline, -1):
            answer[i][len(answer[i]) - 1 - answer[i][::-1].index(0)] = currentNum
            currentNum += 1
            if currentNum == max_num + 1:
                break
        startidx += 1
        startline += 2
        endline -= 1
        size -= 3
    
    return list(chain(*answer))