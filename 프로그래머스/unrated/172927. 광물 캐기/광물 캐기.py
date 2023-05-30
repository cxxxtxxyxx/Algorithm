# """
# 다이아 곡괭이 - 다이아, 철, 돌 1씩
# 철 곡괭이 - 다이아 5, 철 1, 돌 1
# 돌 곡괭이 - 다이아 25, 철 5, 돌 1
# 각 곡괭이는 종류 상관없이 광물 5개 캐면 끝
# 한 번 곡괭이 사용하면 5개 다 캐야됨
# 광물은 주어진 순서대로 캐기
# 모든 광물 캐거나 or 더 이상 곡괭이 없을 때까지 광물캐기
# 최소한의 피로도를 return
# """


from functools import reduce
from collections import Counter
def solution(picks, minerals):
    answer = 0
    mineral_value = {"diamond":25, "iron":5, "stone":1}
    DIAMOND, IRON, STONE = picks[0], picks[1], picks[2]
    DIAMOND_t, IRON_t, STONE_t = picks[0], picks[1], picks[2]
    sort_mineral = []
    
    
    for i in range(0, len(minerals), 5):
        current_minerals = []
        if i + 5 >= len(minerals):
            current_minerals = minerals[i:]
        else: current_minerals = minerals[i:i+5]
        sort_mineral.append(current_minerals)
        
    if sum(picks) >= len(minerals) // 5:
        sort_mineral.sort(key=lambda x: (-reduce(lambda acc, cur: acc + mineral_value[cur], x, 0), -len(x)))
    
    
    for current_minerals in sort_mineral:
        if "diamond" in current_minerals:
            counter = Counter(current_minerals)
            if DIAMOND_t != 0:
                DIAMOND_t -= 1
                answer += len(current_minerals)
            else:
                if IRON_t != 0:
                    IRON_t -= 1
                    dia_count = counter["diamond"]
                    answer += dia_count * 5 + (len(current_minerals) - dia_count)
                else:
                    if STONE_t != 0:
                        STONE_t -= 1
                        dia_count = counter["diamond"]
                        iron_count = counter["iron"]
                        answer += dia_count * 25 + iron_count * 5 + (len(current_minerals) - dia_count - iron_count)
                    else:
                        return answer
        elif "iron" in current_minerals:
            counter = Counter(current_minerals)
            if IRON_t != 0:
                IRON_t -= 1
                dia_count = counter["diamond"]
                answer += dia_count * 5 + (len(current_minerals) - dia_count)
            else:
                if STONE_t != 0:
                    STONE_t -= 1
                    dia_count = counter["diamond"]
                    iron_count = counter["iron"]
                    answer += dia_count * 25 + iron_count * 5 + (len(current_minerals) - dia_count - iron_count)
                else:
                    if DIAMOND_t != 0:
                        DIAMOND_t -= 1
                        answer += len(current_minerals)
                    else:
                        return answer
        else:
            counter = Counter(current_minerals)
            if STONE_t != 0:
                STONE_t -= 1
                dia_count = counter["diamond"]
                iron_count = counter["iron"]
                answer += dia_count * 25 + iron_count * 5 + (len(current_minerals) - dia_count - iron_count)
            else:
                if IRON_t != 0:
                    IRON_t -= 1
                    answer += len(current_minerals)
                else:
                    if DIAMOND_t != 0:
                        DIAMOND_t -= 1
                        answer += len(current_minerals)
                    else:
                        return answer
    return answer
                        