import sys

input = sys.stdin.readline

_arr = list(map(int, input().split()))
res = ''
if _arr[0] < _arr[1]:
    res = 'ascending'
else:
    res = 'descending'

for idx in range(1, len(_arr) - 1):
    if res == 'ascending':
        if _arr[idx] > _arr[idx + 1]:
            print('mixed')
            exit(0)
    else:
        if _arr[idx] < _arr[idx + 1]:
            print('mixed')
            exit(0)

print(res)