import sys


input = sys.stdin.readline

n, m = list(map(int, input().split()))

sequence = []

def get_sequence():
    if len(sequence) == m:
        print(*sequence)
        return

    for i in range(1, n + 1):
        if not i in sequence:
            if len(sequence) == 0:
                sequence.append(i)
                get_sequence()
                sequence.pop()
            else:
                if sequence[-1] < i:
                    sequence.append(i)
                    get_sequence()
                    sequence.pop()

get_sequence()