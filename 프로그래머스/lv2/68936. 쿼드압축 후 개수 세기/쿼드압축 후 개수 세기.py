from itertools import chain
def solution(arr):
    answer = []
    
    # step1: 4개로 쪼개기
    # step2: 각 부분에 대해 모두 같은 수인지 판별한 후
    # step3: 같은 수이면 하나로 통일, 아니면 4개로 쪼갬
    # step4: 배열의 길이가 1이라면 리턴, 아니라면 반복
    split_array(arr, answer)
    return [len(list(filter(lambda x: x == 0, answer))), len(list(filter(lambda x: x == 1, answer)))]

def split_array(arr, answer):
    if all(list(map(lambda x: x == 1, list(chain(*arr))))):
        answer.append(1)
        return
    
    if all(list(map(lambda x: x == 0, list(chain(*arr))))):
        answer.append(0)
        return
    
    arr1 = [arr[i][:len(arr) // 2] for i in range(len(arr) // 2)]
    arr2 = [arr[i][len(arr) // 2:] for i in range(len(arr) // 2)]
    arr3 = [arr[i][:len(arr) // 2] for i in range(len(arr) // 2, len(arr))]
    arr4 = [arr[i][len(arr) // 2:] for i in range(len(arr) // 2, len(arr))]
    split_array(arr1, answer)
    split_array(arr2, answer)
    split_array(arr3, answer)
    split_array(arr4, answer)
    
    
    