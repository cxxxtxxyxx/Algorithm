# 시간 초과
# from functools import reduce

# def get_total_divisor(n):
#   result = []
#   for i in range(1, int(n ** 0.5) + 1):
#     if n % i == 0:
#       result.append(i)
#       if not (n // i) in result:
#         result.append(n // i)
#   return reduce(lambda x, y: x + y, result)

# def get_result(n):
#   return reduce(lambda x, y: x + get_total_divisor(y), range(1, n + 1))

# n = int(input())
# print(get_result(n))


# 배수와 약수의 관계를 이용하여 시간복잡도 줄이기!
# ex
"""
N = 10일 때
1의 배수는 항상 1을 약수로 가진다 1, 2, 3, 4, ..., 10
2의 배수는 항상 2를 약수로 가진다 2, 4, 6, 8, ... , 19
3의 배수는 항상 3을 약수로 가진다 3, 6, 9
4의 배수는 항상 4를 약수로 가진다 4, 8
.. etc
따라서 1부터 10까지 각 수가 들어가는 수 만큼 (10 // i) 하여 거기에 약수를 곱한뒤 모두 더해주면 됨
"""
import sys
input = sys.stdin.readline
n = int(input())

sum_ = 0
for i in range(1, n + 1):
  sum_ += (n // i) * i
print(sum_)