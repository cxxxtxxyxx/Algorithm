import sys

input = sys.stdin.readline

N = int(input())

cranes = list(map(int, input().split()))
cranes.sort(reverse=True)
M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    exit()

answer = 0

while len(boxes) > 0:

    answer += 1

    for crane in cranes:
        for j in range(len(boxes)):
            if crane >= boxes[j]:
                del boxes[j]
                break

print(answer)
