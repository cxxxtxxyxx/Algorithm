"""
자카드 유사도 = 교집합 크기 / 합집합 크기
모두 공집합일 때 1
다중집합 {1, 1, 1}, {1, 1, 1, 1, 1} = 교집합 min(3, 5) 합집합 max(3, 5)
두글자씩 끊어서 다중 집합 만듦
공백, 숫자, 특수문자 들어있는 경우 해당 쌍을 버림
대소문자 구별 x
"""
from collections import Counter
from collections import defaultdict

def get_similar(str1, str2):
    str1_count = defaultdict(int)
    str2_count = defaultdict(int)
    
    for ch in str1:
        str1_count[ch] += 1
        
    for ch in str2:
        str2_count[ch] += 1
    inter = 0
    union = 0
    check = set()
    for ch in str1_count.keys():
        if ch in str2:
            inter += min(str1_count[ch], str2_count[ch])
        union += max(str1_count[ch], str2_count[ch])
        check.add(ch)
        
    for ch in str2_count.keys():
        if ch not in check:
            union += max(str1_count[ch], str2_count[ch])
            
    
                
    return inter / union
            
        
    
def solution(str1, str2):
    
    if str1 == "" and str2 == "":
        return 65536
    alpha = "abcdefghijklmnopqrstuvwxyz"
    str1 = str1.lower()
    str2 = str2.lower()
    # step 1: 자카드 유사도 구하는 함수 구현
    
    # step 2: 주어진 문자열 2글자씩 자르기 (숫자, 공백, 특수문자 제외시키기)
    s1 = []
    s2 = []
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            s1.append(str1[i:i+2])
        
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            s2.append(str2[i:i+2])
        
    if len(s1) == 0 and len(s2) == 0:
        return 65536
    
    # step 3: 자카드 유사도에 65536곱하고 소수점 버린 뒤 리턴
    return int(get_similar(s1, s2) * 65536)