import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

count = 0
answer = 0
i = 0

while i < M - 1:
    if S[i : i + 3] == "IOI":
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
        
        continue

    i += 1
    count = 0

print(answer)