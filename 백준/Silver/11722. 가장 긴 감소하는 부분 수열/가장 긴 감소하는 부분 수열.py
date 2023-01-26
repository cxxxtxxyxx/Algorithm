import sys

input = sys.stdin.readline

n = int(input())

num_arr = list(map(int, input().split()))
result = [1] * n

for i in range(1, n):
    for j in range(i):
        if num_arr[j] > num_arr[i]:
            result[i] = max(result[i], result[j] + 1)


print(max(result))