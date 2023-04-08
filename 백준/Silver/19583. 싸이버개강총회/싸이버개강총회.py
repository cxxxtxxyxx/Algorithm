import sys

input = sys.stdin.readline

S, E, Q = input().split()


res = dict()
while True:
    try:
        time, name = input().split()
        if "00:00" <= time <= S:
            res[name] = False

        if (E <= time <= Q) and name in res:
            res[name] = True
    except:
        print(len(list(filter(lambda x: x == True, list(res.values())))))
        break