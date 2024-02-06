def IsPointInSquare(x, y):
    return x <= 1 and y <= 1 and x >= -1 and y >= -1


a, b = float(input()), float(input())
if IsPointInSquare(a, b):
    print('YES')
else:
    print('NO')
