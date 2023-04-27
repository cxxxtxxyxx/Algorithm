# 메모리 초과
# from itertools import combinations

# n, m = map(int, input().split())
# result = list(combinations([i for i in range(1, n + 1)], m))
# size = list(str(len(result)))

# cnt = 0

# for i in range(len(size) - 1, 1, -1):
#   if size[i] == '0':
#     cnt += 1
#   else:
#     break

# print(cnt)



"""
팩토리얼 내에 들어있는 인수 구하는 법
1. 구하려는 숫자로 나눠주고 몫 더하기
2. 몫 제곱한 후 
3. 1~ 2 반복
"""

def cnt_number(n, k):
  if n == 0:
    return 0
  cnt = 0
  div = k
  while n >= div:
    cnt += (n // div)
    div *= k
    
  return cnt

n, m = map(int, input().split())
num2_cnt = cnt_number(n, 2) - cnt_number(m, 2) - cnt_number(n - m, 2)
num5_cnt = cnt_number(n, 5) - cnt_number(m, 5) - cnt_number(n - m, 5)
print(min(num2_cnt, num5_cnt))