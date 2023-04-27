def binary_search(array, value, low, high):
  if low > high:
    print(0)
    return False
  
  mid = (low + high) // 2
  if array[mid] > value:
    binary_search(array, value, low, mid - 1)
  
  elif array[mid] < value:
    binary_search(array, value, mid + 1, high)

  elif array[mid] == value:
    print(1)

N = int(input())
test_case = list(map(int, input().split(' ')))
test_case.sort()


M = int(input())
test = list(map(int, input().split(' ')))


for i in range(0, len(test)):
  binary_search(test_case, test[i], 0, len(test_case) - 1)