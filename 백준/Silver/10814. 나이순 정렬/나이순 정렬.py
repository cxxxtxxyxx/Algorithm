import sys

input = sys.stdin.readline

n = int(input().strip())

result = [[] for __ in range(201)]
for __ in range(n):
    _idx, _input = input().strip().split()
    result[int(_idx)].append(_input)


for idx, item in enumerate(result):
    for el in item:
        print(idx, el)
