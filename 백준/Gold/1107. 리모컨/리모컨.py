N = int(input())
M = int(input())

button = {str(x) for x in range(10)}

if M != 0:
    button -= set(input().split())


min_cnt = abs(100 - N)

for k in range(1_000_000):
    num = str(k)

    for i in range(len(num)):
        if num[i] not in button:
            break

        if i == len(num) - 1:
            min_cnt = min(min_cnt, abs(N - k) + len(num))

print(min_cnt)