"""
일정 금액 지불시 10일 간 회원 자격 부여
회원 대상으로 매일 한가지 제품 할인
할인 제품은 하루에 하나씩만 구매 가능
해당 범위 내에 모든 제품이 만족하는지
ex 바나나 3 / 사과 2 / 쌀 2 / 돼지고기 2 / 냄비 1
       3        2    2    2 1
        4     2       2   2 1
    3      2        2   2   1
"""

from collections import defaultdict

def check(discount_cnt, want, number):
    cnt = 0
    for i in range(len(want)):
        if discount_cnt[want[i]] == number[i]:
            cnt += 1
            
    return len(number) == cnt
            

def solution(want, number, discount):
    answer = 0
    
    # step 1: start ~ end (10) 만큼 개수 세기
    # 조건 만족시 answer += 1
    # dict[start] -= 1
    # dict[end] += 1
    
    discount_cnt = defaultdict(int)
    
    for i in range(10):
        discount_cnt[discount[i]] += 1
        
  
    start = 0
    end = 9
    while end < len(discount):
        if check(discount_cnt, want, number):
            answer += 1
            
        discount_cnt[discount[start]] -= 1
        start += 1
        end += 1
        
        if end >= len(discount):
            break
            
        discount_cnt[discount[end]] += 1
        
    
    return answer