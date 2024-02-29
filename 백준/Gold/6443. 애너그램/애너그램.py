# 6443 G5

import sys

input = sys.stdin.readline

N = int(input().strip())

def backtracking(word, visited, tmp):

    if len(tmp) == len(word):
        print("".join(tmp))
        return
    
    for i in visited:
        if visited[i]:
            visited[i] -= 1
            tmp.append(i)
            backtracking(word, visited, tmp)
            tmp.pop()
            visited[i] += 1


for __ in range(N):

    word = sorted(list(input().strip()))

    visited = dict()

    for w in word:
        if w in visited:
            visited[w] += 1
        else:
            visited[w] = 1

    backtracking(word, visited, [])

