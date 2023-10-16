import numpy as np

def solution(a, b):
    aa = np.array(a)
    bb = np.array(b)
    return sum(list(map(int, aa * bb)))