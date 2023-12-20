import sys
import math

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
numsLength = len(nums)

subtractMods = []
result = []

for idx in range(numsLength -1):
    subtractMods.append(abs(nums[idx + 1] - nums[idx]))


_gcd = math.gcd(*subtractMods)

for idx in range(2, _gcd + 1):
    if(_gcd % idx == 0):
        result.append(idx)

print(*result)
