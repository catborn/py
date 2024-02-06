from math import ceil, floor
x = float(input())
okr = floor(x)
dr = x - okr
if dr == 0.5:
    print(okr + 1)
elif dr > 0.5:
    print(ceil(x))
elif dr < 0.5:
    print(okr)
