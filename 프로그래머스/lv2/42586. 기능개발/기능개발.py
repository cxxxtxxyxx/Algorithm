from collections import deque
def solution(progresses, speeds):
    answer = []
    
    length = len(progresses)
    days = deque([])
    stack = []

    for idx in range(length):
        if (100 - progresses[idx]) % speeds[idx] == 0:
            days.append((100 - progresses[idx]) // speeds[idx])
        else:
            days.append((100 - progresses[idx]) // speeds[idx] + 1)

    count = 1
    current_num = 0
    for day in list(days):
        print(day, count)
        if not stack:
            stack.append(day)
            continue
        if stack[-1] >= day:
            count += 1
        else:
            answer.append(count)
            while stack:
                stack.pop()
            stack.append(day)
            count = 1
        # else:
        #     answer.append(count + 1)
        #     while stack:
        #         stack.pop()
        #     stack.append(day)
        #     count = 1
    answer.append(count)
    #     while stack and stack[-1] > day:
    #         count += 1
        
    #     if stack and stack[-1] < day:
    #         print(count)
    #         answer.append(count)
    #         stack = []
    #         count = 1
    #     else:
    #         stack.append(day)

    # answer.append(len(stack))

    # answer.append(len(stack))


    return answer