import sys
import math
from functools import reduce

input = sys.stdin.readline

n = int(input())
a = reduce(lambda x, y: x * y, list(map(int, input().split())))
m = int(input())
b = reduce(lambda x, y: x * y, list(map(int, input().split())))

_gcd = math.gcd(a, b)

_gcd_str = str(_gcd)
_len = len(_gcd_str)

if _len > 9:
    print(_gcd_str[_len - 9:])

else:
    print(_gcd_str)