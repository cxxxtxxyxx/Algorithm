import sys
import copy

input = sys.stdin.readline

n = int(input())

num_arr = list(map(int, input().split()))

res = copy.deepcopy(num_arr)

for i in range(1, n):
    for j in range(i):
        if num_arr[i] > num_arr[j]:
            res[i] = max(res[i], res[j] + num_arr[i])

print(max(res))

