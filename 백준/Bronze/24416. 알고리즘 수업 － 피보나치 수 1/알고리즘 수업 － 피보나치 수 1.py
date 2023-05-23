import sys

input = sys.stdin.readline

count_fib = 0
count_fibonacci = 0

n = int(input())

def fib(n):
    global count_fib
    if n == 1 or n == 2:
        count_fib += 1

        return 1
    
    return fib(n - 1) + fib(n - 2)


dp = [0] * (n + 1)
def fibonacci(n):
    global count_fibonacci
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        count_fibonacci += 1
    return dp[n]

fib(n)
fibonacci(n)

print(count_fib, count_fibonacci)