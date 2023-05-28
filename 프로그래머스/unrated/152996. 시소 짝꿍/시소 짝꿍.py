"""
거리 2, 3, 4
탑승 사람 무게 * 좌석간 거리의 곱이 양쪽 다 같다면 시소 짝궁
"""

from collections import Counter
def solution(weights):
    answer = 0
    # rate = [(1, 1), (1, 2), (2, 3), (3, 4), (2, 1), (3, 2), (4, 3)]
    
    count = Counter(weights)
    for key in dict(count).keys():
        if count[key] >= 0:
            answer += (count[key] - 1) * count[key] // 2 # 같은 값
            answer += count[key] * count[key * 2]
            answer += count[key] * count[key * 4 / 3]
            answer += count[key] * count[key * 3 / 2]
                
    
    
    return answer