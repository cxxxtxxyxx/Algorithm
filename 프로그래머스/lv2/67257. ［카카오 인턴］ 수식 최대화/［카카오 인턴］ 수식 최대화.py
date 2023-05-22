def solution(expression):
    answer = 0
    _max = 0
    cases = ["*+-", "*-+", "+*-", "+-*", "-*+", "-+*"]
    
    split_exp = split_expression(expression)
    
    for case in cases:
        tmp = split_exp[:]
        for c in case:
            while c in tmp:
                op_idx = tmp.index(c)
                tmp = tmp[:op_idx-1] + [calc(tmp[op_idx], tmp[op_idx-1], tmp[op_idx+1])] + tmp[op_idx+2:]
            
        _max = max(_max, abs(tmp[0]))
    return _max

def calc(c, a, b):
    if c == "*":
        return a * b
    
    if c == "+":
        return a + b
    
    if c == "-":
        return a - b
    
def split_expression(expression):
    stack = []
    prev = 0
    for i in range(len(expression)):
        if expression[i].isdigit():
            continue
        
        stack.append(int(expression[prev:i]))
        stack.append(expression[i])
        prev = i + 1
    stack.append(int(expression[prev:]))
    return stack