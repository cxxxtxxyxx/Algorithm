import sys

input = sys.stdin.readline

word = input().strip()


for i in range(1, 13):
    stand = 'w' * i + 'o' * i + 'l' * i + 'f' * i
    while word.find(stand) != -1:
        word = word.replace(stand, 'x')

reslen = len(list(filter(lambda x: x != 'x', list(word))))


if reslen == 0:
    print(1)

else:
    print(0)

