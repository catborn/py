def sum(a, b):
    if a == 0 or b == 0:
        return b or a
    elif a >= 0 and b >= 0:
        return sum(a + 1, b - 1)


print(sum(int(input()), int(input())))
