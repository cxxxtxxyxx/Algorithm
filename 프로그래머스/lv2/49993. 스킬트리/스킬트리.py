import re
def solution(skill, skill_trees):
    cnt = 0
    
    
    for skill_tree in skill_trees:
        res = re.sub("[^" + skill + "]", "", skill_tree)
        if res in skill and skill.find(res) == 0:
            cnt += 1
        
    return cnt