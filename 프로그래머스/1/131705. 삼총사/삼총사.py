def solution(number):
    answer = 0
    arr = []
    
    answer = dfs(arr, answer, 0, [], number)
        
    return len(list(filter(lambda x: sum(x) == 0, arr)))

def dfs(arr, count, idx, list, number):
    if len(list) == 3:
        if sum(list) == 0:
            arr.append(list)
        return

    for i in range(idx, len(number)):
        dfs(arr, count, i+1, list + [number[i]], number)
        
    return;