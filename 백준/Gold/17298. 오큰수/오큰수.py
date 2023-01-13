import sys

n = int(input().strip())

a = list(map(int, input().strip().split()))

length = len(a)
stack = []
result = [-1] * length
current_num = 0
for idx in range(0, length):  
    while stack and stack[-1][1] < a[idx]:
        got_item = stack.pop()
        result[got_item[0]] = a[idx]

    stack.append((idx, a[idx]))
    
print(*result)