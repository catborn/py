def min4(a, b, c, d):
    ab = min(a, b)
    cd = min(c, d)
    ac = min(ab, cd)
    return ac


a1, b1, c1, d1 = int(input()), int(input()), int(input()), int(input())
print(min4(a1, b1, c1, d1))
