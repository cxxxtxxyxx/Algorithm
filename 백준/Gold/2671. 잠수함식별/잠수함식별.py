import re
import sys

input = sys.stdin.readline

# (100~1~|01)~

regex = re.compile(r'(100{1,}1{1,}|01){1,}')

_input = input().strip()

if regex.fullmatch(_input):
    print("SUBMARINE")
    exit()

print("NOISE")