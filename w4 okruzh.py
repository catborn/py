def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


a, b = float(input()), float(input())
c, d, e = float(input()), float(input()), float(input())
if IsPointInCircle(a, b, c, d, e):
    print('YES')
else:
    print('NO')
