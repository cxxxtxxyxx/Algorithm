import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())

highway = list(map(int, input().split()))
highway.append(0)
highway.append(L)
highway.sort()


def binary_search():
    start = 1
    end = L

    while start <= end:
        count = 0
        mid = (start + end) // 2

        for i in range(len(highway) - 1):
            if highway[i + 1] - highway[i] > mid and mid != 0:
                num = (highway[i + 1] - highway[i] - 1) // mid
                count += num
                
        if count <= M:
            end = mid - 1
            res = mid

        else:
            start = mid + 1

    return res


print(binary_search())