import sys

input = sys.stdin.readline

T = int(input().strip())


def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def get_prime_nums():
    MAX_SIZE = 10_001
    prime_nums = [False] * MAX_SIZE

    prime_nums[1] = False
    prime_nums[2] = True

    for i in range(2, MAX_SIZE):
        if isPrime(i) == True:
            prime_nums[i] = True
            for j in range(i * 2, MAX_SIZE, i):
                prime_nums[j] = False

        

    return prime_nums

result = get_prime_nums()

for __ in range(T):
    n = int(input().strip())

    half = n // 2

    if result[half]:
        print(half, half)
        continue

    
    left = half
    right = half

    if half % 2 == 0:
        left -= 1
        right += 1

    while not result[left] or not result[right]:
        left -= 2
        right += 2

    print(left, right)