import sys

input = sys.stdin.readline

def getSolution(n):
    res = []

    for i in range(3 * len(n)):
        if i // len(n) == 1:
            res.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            res.append(n[i % len(n)] * 3)
    
    return res

star = ["***", "* *", "***"]

n = int(input())
cnt = 0

while n != 3:
    n //= 3
    cnt += 1

for __ in range(cnt):
    star = getSolution(star)

for i in star:
    print(i)

