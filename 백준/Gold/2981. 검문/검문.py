import sys
import math
input = sys.stdin.readline

# 시간 제한: 1초

# 근처에 보이는 숫자 N개를 종이에 적는다
# 종이에 적은 수를 M으로 나누었을 때,
# 나머지가 모두 같게 되는 M을 모두 찾으려고 한다
# M > 1

# 첫째 줄에 종이에 적은 수의 개수 N이 주어진다 (2 <= N <= 100)

# 다음 줄부터 N개 줄에는 종이에 적은 수가 하나씩 주어진다
# 1 <= 수 <= 1,000,000,000

# ex
# 3 - 6, 34, 38
# 가능한 M -> 2, 4
# 0, 0 ,0
# 2, 2, 2

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

gcds = []
result = []


for i in range(len(nums) - 1):
    gcds.append(nums[i + 1] - nums[i])

_gcd = math.gcd(*gcds)

for x in range(2, _gcd + 1):
    if _gcd % x == 0:
        result.append(x)

print(*result)
