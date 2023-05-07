# import re
# def solution(skill, skill_trees):
#     cnt = 0
    
    
#     for skill_tree in skill_trees:
#         res = re.sub("[^" + skill + "]", "", skill_tree)
#         if res in skill and skill.find(res) == 0:
#             cnt += 1
        
#     return cnt


from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = deque(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.popleft():
                    break
        else:
            answer += 1

    return answer
