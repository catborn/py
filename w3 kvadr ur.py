a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
if d >= 0:
    x1 = (- b - d ** 0.5) / (2 * a)
    x2 = (- b + d ** 0.5) / (2 * a)
    if x1 == x2:
        print(x1)
    elif x1 > x2:
        print(x2, x1)
    elif x2 > x1:
        print(x1, x2)
elif d < 0:
    print()
