import sys

input = sys.stdin.readline

X, Y = map(int, input().split())

diff = Y - X

if diff == 0:
    print(0)
else:
    if int((diff) ** 0.5) ** 2 == diff:
        print(int((diff) ** 0.5) * 2 - 1)

    else:
        integer = int(diff ** 0.5) ** 2
        if diff - integer <= int(diff ** 0.5):
            print(int(diff ** 0.5) * 2)
        else:
            print(int(diff ** 0.5) * 2 + 1)


