import sys


input = sys.stdin.readline


res = [0, 1, 2, 4, 7] + [0] * 6

for i in range(5, 11):
    res[i] = res[i - 1] + res[i - 2] + res[i - 3]


t = int(input())

for __ in range(t):
    target = int(input())
    print(res[target])


""" 1 2 4 7 13 24 44 77 
         
f(1) = 1
f(2) = 2
f(3) = 4
f(4) = 7
---
f(5) = 13
1 1 1 1 1 O
1 1 1 2
1 1 2 1
1 2 1 1
2 1 1 1
1 2 2 
2 1 2
2 2 1
2 3
3 2
3 1 1
1 3 1
1 1 3
---
f(6) = 24
1 1 1 1 1 1
1 1 1 1 2
1 1 1 2 1
1 1 2 1 1
1 2 1 1 1
2 1 1 1 1
1 1 2 2
1 2 1 2
1 2 2 1
2 1 2 1
2 2 1 1
2 1 1 2
3 3
1 1 1 3
1 1 3 1
1 3 1 1
3 1 1 1
1 2 3 
1 3 2
2 1 3
2 3 1
3 1 2 
3 2 1
2 2 2
"""