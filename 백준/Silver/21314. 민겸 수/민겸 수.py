import re
import sys

input = sys.stdin.readline

mkstr = input().strip()
length = len(mkstr)
_max = ''
_min = ''

count = 0
for char in mkstr:
    if char == "M":
        count += 1
    else:
        if count > 0:
            _max += str(5 * 10 ** count)
            _min += str(10 ** count + 5)
        else:
            _max += '5'
            _min += '5'
        count = 0
        
if count != 0:
    _max += '1' * count
    _min += str(10 ** (count - 1))

print(_max)
print(_min)

