import sys

input = sys.stdin.readline


def get_primes():
    MAX_SIZE = 1_000_001
    primes = [True] * MAX_SIZE

    primes[0] = primes[1] = False

    for i in range(2, MAX_SIZE):
        if primes[i] == True:
            for j in range(i * 2, MAX_SIZE, i):
                primes[j] = False

    return primes


primes = get_primes()
while True:

    N = int(input().strip())

    if N == 0:
        break

    flag = False
    for i in range(len(primes)):
        if primes[i]:
            if primes[N - i]:
                print(f'{N} = {i} + {N - i}')
                flag = True
                break

    if flag == False:
        print("Goldbach's conjecture is wrong.")
