import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().strip().split())

words = [set(list(input().strip())) for __ in range(N)]

if K < 5:
    print(0)
    exit()

alpha_dict = defaultdict(int)
for ch in ('a', 'c', 't', 'i', 'n'):
    alpha_dict[ch] = 1

result = 0
def backtracking(idx, depth):

    global result

    if depth == K:
        _sum = 0
        alphas = set(list(filter(lambda x: alpha_dict[x] == 1, alpha_dict.keys())))
        for word in words:
            if alphas.issuperset(word):
                _sum += 1
        
        result = max(result, _sum)
        return 

    

    for i in range(idx, 26):
        if chr(ord('a') + i) not in alpha_dict or alpha_dict[chr(ord('a') + i)] == 0:
            alpha_dict[chr(ord('a') + i)] = 1
            backtracking(i + 1, depth + 1)
            alpha_dict[chr(ord('a') + i)] = 0


backtracking(0, 5)
print(result)