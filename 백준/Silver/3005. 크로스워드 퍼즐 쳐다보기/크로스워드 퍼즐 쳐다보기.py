import sys

input = sys.stdin.readline

R, C = map(int, input().split())

puzzle = [input().strip() for __ in range(R)]

total_word = ""

for word in puzzle:
    total_word += word
    total_word += "#"

for i in range(C):
    for j in range(R):
        total_word += puzzle[j][i]
    total_word += "#"

total_word = total_word.split("#")
total_word.sort()

for word in total_word:
    if len(word) >= 2:
        print(word)
        exit()