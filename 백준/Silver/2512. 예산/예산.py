import sys

input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
country_budget = int(input())

def binary_search():
    start = 1
    end = max(budgets)
    res = 0
    while start <= end:
        mid = (start + end) // 2

        total = sum(map(lambda x: x if mid >= x else mid, budgets))

        if total > country_budget:
            end = mid - 1

        else:
            res = mid
            start = mid + 1

    return res

print(binary_search())

    