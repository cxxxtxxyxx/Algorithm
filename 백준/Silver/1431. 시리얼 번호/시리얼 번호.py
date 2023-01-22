import sys

input = sys.stdin.readline

n = int(input().strip())

_input = [input().strip() for __ in range(n)]

length = len(_input)

def getDigitSum(str):
    _sum = 0
    for char in str:
        if "0" <= char <= "9":
            _sum += int(char)
    
    return _sum


for i in range(length - 1):
    for j in range(length - 1):
        if len(_input[j]) > len(_input[j + 1]):
            _input[j], _input[j + 1] = _input[j + 1], _input[j]
        elif len(_input[j]) == len(_input[j + 1]):
            if len(_input[j]) == len(_input[j + 1]):
                if getDigitSum(_input[j]) > getDigitSum(_input[j + 1]):
                    _input[j], _input[j + 1] = _input[j + 1], _input[j]
                elif getDigitSum(_input[j]) == getDigitSum(_input[j + 1]):
                    if _input[j] > _input[j + 1]:
                        _input[j], _input[j + 1] = _input[j + 1], _input[j]
            

for el in _input:
    print(el)