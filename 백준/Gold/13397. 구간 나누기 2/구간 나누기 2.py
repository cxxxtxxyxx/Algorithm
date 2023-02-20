import sys

input = sys.stdin.readline


# N = size, M = 구간 개수
N, M = map(int, input().split())

nums = list(map(int, input().split()))


# range => 0 <= x <= max(nums) - 1


def binary_search():
    start = 0
    end = max(nums)

    res = end

    while start <= end:
        mid = (start + end) // 2
        b_s = 0
        b_e = 0
        cnt = 1

        while 0 <= b_s < N and 0 <= b_e < N:
            if max(nums[b_s:b_e+1]) - min(nums[b_s:b_e+1]) > mid:
                cnt += 1
                b_s = b_e
            else:
                b_e += 1

        if cnt <= M:

            end = mid - 1

            res = min(res, mid)

        elif cnt > M:
            start = mid + 1



    return res

print(binary_search())




