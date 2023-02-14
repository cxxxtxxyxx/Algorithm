import sys
input = sys.stdin.readline

getMax = 0
def binarySearch(start, end):
    global getMax
    global cables
    if start > end:
        return getMax
    
    mid = (start + end) // 2
    totalCount = getTotalCableCount(cables, mid)

    if totalCount < N:
        return binarySearch(start, mid - 1)
    else:
        getMax = mid
        return binarySearch(mid + 1, end)

def getTotalCableCount(cables, value):
    res = 0
    for cable in cables:
        res += cable // value
    return res

K, N = map(int, input().split())

cables = [int(input()) for _ in range(K)]

maxLength = max(cables)

print(binarySearch(1, maxLength))