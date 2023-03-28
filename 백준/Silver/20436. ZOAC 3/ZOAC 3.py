import sys

input = sys.stdin.readline

keyboard = []
key1 = "qwertyuiop"
key2 = "asdfghjkl"
key3 = "zxcvbnm"

keyboard.append(list(key1))
keyboard.append(list(key2))
keyboard.append(list(key3))

lhand, rhand = input().strip().split()
write = list(input())
lx, ly = 0, 0
rx, ry = 0, 0
for i in range(3):
    for j in range(len(keyboard[i])):
        if keyboard[i][j] == lhand:
            lx, ly = i, j

        if keyboard[i][j] == rhand:
            rx, ry = i, j

left = "qwertasdfgzxcv"
right = "yuiophjklbnm"

def getDist(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

count = 0
for w in write:
    if w == lhand or w == rhand:
        count += 1
    else:
        if w in left:
            for i in range(3):
                for j in range(len(keyboard[i])):
                    if keyboard[i][j] == w:
                        lhand = keyboard[i][j]
                        count += getDist(lx, i, ly, j) + 1
                        lx, ly = i, j

        if w in right:
            for i in range(3):
                for j in range(len(keyboard[i])):
                    if keyboard[i][j] == w:
                        rhand = keyboard[i][j]
                        count += getDist(rx, i, ry, j) + 1
                        rx, ry = i, j

                        
    
print(count)
