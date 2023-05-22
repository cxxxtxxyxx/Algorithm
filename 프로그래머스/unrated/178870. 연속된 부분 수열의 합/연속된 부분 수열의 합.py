# import sys
# def solution(sequence, k):
#     answer = [0, 0]
#     _min = sys.maxsize
    
#     start = 0
#     end = 0
#     _sum = sequence[0]
#     n = len(sequence)
#     while end < n:
#         if _sum == k and _min > end - start + 1:
#             _min = end - start + 1
#             answer[0] = start
#             answer[1] = end
            
#         elif _sum > k:
#             start += 1
#             _sum -= sequence[start - 1]
#             continue
            
#         end += 1
#         if end >= n:
#             break
#         _sum += sequence[end]
#     return answer

# def solution(sequence, k):
#     answer = []

#     start, end = 0, 0
#     acc = sequence[0]

#     min_len = 2147483647
#     while start <= end < len(sequence):
#         if start > end:
#             acc = sequence[start]
#             end = start
#             continue

#         if acc == k:
#             if min_len > end - start + 1:
#                 min_len = end - start + 1
#                 answer = [start, end]
#             acc -= sequence[start]
#             start += 1
#         elif acc > k:
#             acc -= sequence[start]
#             start += 1
#         elif acc < k:
#             end += 1
#             if end < len(sequence):
#                 acc += sequence[end]

#     return answer


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
def solution(sequence, k):
    answer = []
    # start = 0
    end = 0
    interval_sum = 0
    lenth = 10000000

    for start in range(len(sequence)):
        while interval_sum < k and end < len(sequence):
            interval_sum += sequence[end]
            end += 1

        if interval_sum == k and end - start < lenth:
            answer = [start,end-1]
            lenth = end - start
        interval_sum -= sequence[start]

    return answer