import sys

input = sys.stdin.readline

n, k = list(map(int, input().strip().split()))

num_list = list(input().strip())

stack = []
count = 0
for idx in range(len(num_list)):
    
    while stack and stack[-1] < num_list[idx] and count != k:
        stack.pop()
        count += 1
    
    stack.append(num_list[idx])

while count != k:
    count += 1
    stack.pop()

print("".join(stack))