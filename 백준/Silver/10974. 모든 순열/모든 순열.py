import sys

input = sys.stdin.readline

n = int(input())
sequence = []

def get_sequence():
    if(len(sequence) == n):
        print(*sequence)
        return

    for i in range(1, n + 1):
        if not i in sequence:
            sequence.append(i)
            get_sequence()
            sequence.pop()
            

get_sequence()
        