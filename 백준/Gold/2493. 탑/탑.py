import sys

input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().strip().split()))

stack = []
result = [0] * n
for i in range(n):
    current_num = nums[i]
    while stack and nums[stack[-1]] < current_num:
        stack.pop()
    
    if stack:
        result[i] = stack[-1] + 1
    
    stack.append(i)

print(*result)
  