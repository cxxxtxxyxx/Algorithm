import sys

input = sys.stdin.readline

N, C = map(int, input().split())

homes = [int(input()) for __ in range(N)]
homes.sort()


def binary_search():
    answer = 0
    start = 1
    end = homes[-1] - homes[0]

    while start <= end:
        count = 1

        mid = (start + end) // 2

        current = homes[0]
        for i in range(1, len(homes)):
            if homes[i] - current >= mid:
                count += 1
                current = homes[i]

        if count >= C:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

if C == 2:
    print(homes[-1] - homes[0])
    exit(0)

print(binary_search())
