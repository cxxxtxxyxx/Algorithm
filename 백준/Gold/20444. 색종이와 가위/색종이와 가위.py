import sys

input = sys.stdin.readline

n, k = map(int, input().split())

res = ''

flag = False
def binary_search():

    start = 0
    end = n // 2
    global flag


    while start <= end:
        row = (start + end) // 2
        col = n - row

        cnt = (row + 1) * (col + 1)

        if cnt == k:
            print("YES")
            flag = True
            break

        if cnt > k:
            end = row - 1


        else:
            start = row + 1

            
binary_search()
if not flag:
    print('NO')
