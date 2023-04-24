def solution(n, words):
    answer = []

    cwords = set()
    
    for idx, word in enumerate(words):
        if word in cwords:
            return [idx % n + 1, idx // n + 1]
        
        if idx != 0 and words[idx - 1][-1] != word[0]:
            return [idx % n + 1, idx // n + 1]
        
        cwords.add(word)
        
    return [0, 0]