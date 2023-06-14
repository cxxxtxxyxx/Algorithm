def solution(cards1, cards2, goal):
    for i in range(len(goal)):
        if cards1 and goal[i] == cards1[0]:
            del cards1[0]
            continue
        
        if cards2 and goal[i] == cards2[0]:
            del cards2[0]
            continue
            
        return "No"
        
    return "Yes"