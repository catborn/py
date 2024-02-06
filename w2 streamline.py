a, b, c = int(input()), int(input()), int(input())
if a >= b >= c:
    print(c, b, a)
elif b >= c >= a:
    print(a, c, b)
elif c >= a >= b:
    print(b, a, c)
elif a <= b <= c:
    print(a, b, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
