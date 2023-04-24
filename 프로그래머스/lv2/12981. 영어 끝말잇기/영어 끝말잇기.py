def solution(n, words):
    answer = []

    cwords = set()
    
    flag = False
    for idx, word in enumerate(words):
        
        if len(word) == 1:
            flag = True
            return [idx % n + 1, len(words) // n]
        
        if word in cwords:
            flag = True
            return [idx % n + 1, len(words) // n]
        
        if idx != 0 and words[idx - 1][-1] != word[0]:
            flag = True
            return [idx % n + 1, len(words) // n]
        
        cwords.add(word)
        
    if flag == False:
        return [0, 0]