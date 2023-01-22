import sys
import copy

input = sys.stdin.readline

n = int(input().strip())

_input = list(map(int, input().split()))

copy_input = list(set(copy.deepcopy(_input)))
copy_input.sort()
res = []
new_dict = {}
for idx, value in enumerate(copy_input):
    new_dict[value] = idx

for el in _input:
    res.append(new_dict[el])


print(*res)