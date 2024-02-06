from math import floor
x = float(input())
c = abs(x)
okr = floor(c)
dr = x - okr
print('{0:.6f}'.format(dr))
