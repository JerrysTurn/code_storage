import math

X, Y = map(int, input().split())
Z = math.floor(Y/X * 100)
count = 0
if Z >= 99:
    print(-1)
else:
    while(True):
        count += 1
        X = X + 1
        Y = Y + 1
        if math.floor(Y/X * 100) >= (Z+1):
            print(count)
            break