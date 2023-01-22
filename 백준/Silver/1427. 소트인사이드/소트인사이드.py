import sys


input = sys.stdin.readline

_input = list(input().strip())


_input.sort(reverse=True)

print("".join(_input))