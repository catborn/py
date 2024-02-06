from math import floor
x = float(input())
c = abs(x)
okr = floor(c)
dr = x - okr
print(okr, '{0:.0f}'.format(dr*100))
