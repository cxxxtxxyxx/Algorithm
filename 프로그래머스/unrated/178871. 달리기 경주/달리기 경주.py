def solution(players, callings):
    place = dict()
    for idx, player in enumerate(players):
        place[player] = idx
        
    for calling in callings:
        idx = place[calling]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        place[players[idx - 1]], place[players[idx]] = place[players[idx]], place[players[idx - 1]]
        
        
    return players