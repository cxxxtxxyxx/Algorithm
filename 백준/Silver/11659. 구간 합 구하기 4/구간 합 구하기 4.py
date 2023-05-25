import sys

input = sys.stdin.readline

N, M = map(int, input().split())

input_list = list(map(int, input().split()))

S = [0 for __ in range(N)]

S[0] = input_list[0]

for i in range(1, N):
    S[i] = S[i - 1] + input_list[i]

for __ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(S[j - 1])
    else:
        print(S[j - 1] - S[i - 2])