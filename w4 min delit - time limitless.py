def mindivisor(n):
    i = 2
    while n % i != 0:
        i = i + 1
    return i


n = int(input())
print(mindivisor(n))
