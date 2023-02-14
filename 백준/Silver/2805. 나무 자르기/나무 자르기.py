import sys
from functools import reduce
input = sys.stdin.readline

def binarySearch(start, end):
    global getMax
    if start > end:
        return getMax
    
    mid = (start + end) // 2
    height = totalSum(mid)

    if(M > height):
        return binarySearch(start, mid - 1)
    else:
        getMax = mid
        return binarySearch(mid + 1, end)

def totalSum(value):
    return reduce(lambda acc, cur: acc + cur - value if(cur - value > 0) else acc + 0, trees, 0)

N, M = map(int, input().split())
trees = list(map(int, input().split()))

maxHeight = max(trees)
getMax = 0

print(binarySearch(0, maxHeight))