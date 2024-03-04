import sys

input = sys.stdin.readline

N = int(input())

result = []
def backtracking(prev, depth):

    if prev:
        num = int("".join(map(str, prev)))
        result.append(num)


    for i in range(10):
        if not prev or prev[-1] > i:
            prev.append(i)
            backtracking(prev, depth + 1)
            prev.pop()


backtracking([], 0)

result = sorted(result)
if len(result) < N:
    print(-1)
else:
    print(result[N - 1])


