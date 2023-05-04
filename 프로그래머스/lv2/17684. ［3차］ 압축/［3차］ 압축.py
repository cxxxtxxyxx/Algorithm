"""
LZW 압축 과정
1. 길이 1인 모든 단어 포함하도록 사전 초기화
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾음
3. w에 해당하는 사전의 인덱스를 출력하고 입력에서 w를 제거
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w + c 에 해당하는 단어를 사전에 등록
5. 단계 2로 돌아감


"""

from collections import defaultdict

def solution(msg):
    answer = []
    
    word = defaultdict(int)
    count = 27
    for i in range(26):
        word[chr(ord('A') + i)] = i + 1
    # Step 1: for문 돌면서 가장 긴 문자열 찾음
    # Step 2: 해당 문자열 인덱스를 answer에 추가
    i = 0
    while i < len(msg):
        end = i + 1
        
        while word[msg[i:end + 1]] != 0 and end + 1 <= len(msg):
            end += 1
        
        answer.append(word[msg[i:end]])
        word[msg[i:end+1]] = count
        count += 1
        i = end
#         end = i + 1
#         prev = ""
#         idx = i
#         while end < len(msg):
#             find_idx = word[msg[i:end]]
#             if find_idx != 0:
#                 end += 1
#                 prev = msg[i:end]
#                 idx = find_idx
#                 continue
            
            
#             answer.append(idx)
#             word[msg[i:end]] = count
#             count += 1
#             break
        
        
#         i += 1
        
        # if end == len(msg):
        #     answer.append(idx)
        #     word[msg[i:end]] = count
        #     count += 1
            
    
    # Step 3: 다음 문자 포함해서 배열에 추가
    # Step 4: 반복
    
    return answer