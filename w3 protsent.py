from math import floor
p, x, y = int(input()), int(input()), int(input())
rub = x + (x/100 * p)
kop = y + (y/100 * p)
sum = rub + (floor(kop)/100)
sumkop = (sum - floor(sum))*100
print(floor(sum), '{0:.0f}'.format(sumkop))
