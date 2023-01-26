import sys

input = sys.stdin.readline

n = int(input())

res = [0] * (n + 1)


# for i in range(5, n + 1):
#     _min = 0
#     if i % 3 == 0 and i % 2 == 0:
#         _min = min(res[i // 3], res[i // 2], res[i - 1])
#         if _min == res[i // 3]:
#             res[i] = 1 + res[i // 3]
#         elif _min == res[i // 2]:
#             res[i] = 1 + res[i // 2]
#         else:
#             res[i] = 1 + res[i - 1]
#     elif i % 3 == 0 and i % 2 != 0:
#         _min = min(res[i // 3], res[i - 1])
#         if _min == res[i // 3]:
#             res[i] = 1 + res[i // 3]
#         else:
#             res[i] = 1 + res[i - 1]
#     elif i % 2 == 0 and i % 3 != 0:
#         _min = min(res[i // 2], res[i - 1])
#         if _min == res[i // 2]:
#             res[i] = 1 + res[i // 2]
#         else:
#             res[i] = 1 + res[i - 1]
#     else:
#         res[i] = 1 + res[i - 1]


for i in range(2, n + 1):
    res[i] = res[i - 1] + 1

    if i % 3 == 0:
        res[i] = min(res[i], res[i // 3] + 1)
    if i % 2 == 0:
        res[i] = min(res[i], res[i // 2] + 1)

    

print(res[n])