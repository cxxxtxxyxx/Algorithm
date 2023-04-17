import sys
from collections import defaultdict

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = [int(input()) for __ in range(N)]

start = 0
end = k - 1
_max = 0
eat = defaultdict(int)

eat[c] += 1

for i in range(k):
    eat[sushi[i]] += 1



while start < N:
    _max = max(_max, len(eat))


    eat[sushi[start]] -= 1

    if eat[sushi[start]] == 0:
        del eat[sushi[start]]


    start += 1
    end += 1

    eat[sushi[end % N]] += 1

    

print(_max)
    
