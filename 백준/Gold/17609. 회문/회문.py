import sys

input = sys.stdin.readline

T = int(input().strip())

def is_palindrome(start, end):
    global string

    while start <= end:

        if string[start] == string[end]:
            start += 1
            end -= 1
            
        else:
            return False
        
    return True

# a c b e b c b a
for __ in range(T):
    string = list(input().strip())

    length = len(string)
    start = 0
    end = length - 1

    flag = False
    res = -1
    while start <= end:
        
        if string[start] == string[end]:
            if not (start + 1 <= end and start <= end - 1):
                break
            start += 1
            end -= 1

        else:
            if (is_palindrome(start + 1, end) or is_palindrome(start, end - 1)):
                res = 1
                break
            else:
                res = 2
                break

    if res == -1:
        res = 0

    print(res)