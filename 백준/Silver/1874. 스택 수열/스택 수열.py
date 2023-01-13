import sys

input = sys.stdin.readline

current_num = 0
flag = 0
PUSH = "+"
POP = "-"
n = int(input().strip())

nums = [int(input().strip()) for __ in range(n)]
result = []
stack = []
for num in nums:
    if num > current_num:
        while True:
            current_num += 1
            stack.append(current_num)
            result.append(PUSH)
            if current_num == num:
                break

    if stack[-1] == num:
        stack.pop()
        result.append(POP)
    else:
        print("NO")
        flag = 1
        break

    
if flag == 0:
    for el in result:
        print(el)