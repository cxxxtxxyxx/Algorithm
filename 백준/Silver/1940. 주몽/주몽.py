import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
uniq_num = sorted(list(map(int, input().split())))

start = 0
end = N - 1
count = 0


while start < end:

    if uniq_num[start] + uniq_num[end] == M:
        count += 1
        end -= 1

        
    elif uniq_num[start] + uniq_num[end] < M:
        start += 1

    else:
        end -= 1

print(count)
