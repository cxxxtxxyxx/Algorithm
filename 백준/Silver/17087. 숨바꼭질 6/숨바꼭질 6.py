import sys
import math

def get_gcd(gcd_arr):
  gcd = math.gcd(gcd_arr[0], gcd_arr[1])
  for i in range(2, len(gcd_arr)):
    gcd = math.gcd(gcd, gcd_arr[i])
  return gcd

N, S = map(int, input().split())

if N == 1:
  print(abs(int(input()) - S))

else:
  get_array = list(map(lambda x: abs(int(x) - S), input().split()))
  print(get_gcd(get_array))

