import sys
import copy

input = sys.stdin.readline

LEFT = "L"
RIGHT = "D"
DELETE = "B"
WRITE = "P"

input_str = list(input().strip())

left_cursor = copy.deepcopy(input_str)
right_cursor = []

m = int(input().strip())

for __ in range(m):
    operator = input().strip().split()

    if operator[0] == LEFT:
        if len(left_cursor) != 0:
            right_cursor.append(left_cursor.pop())
    elif operator[0] == RIGHT:
        if len(right_cursor) != 0:
            left_cursor.append(right_cursor.pop())
    elif operator[0] == DELETE:
        if len(left_cursor) != 0:
            left_cursor.pop()
    else:
        left_cursor.append(operator[1])

right_cursor.reverse()
print("".join(left_cursor + right_cursor))