def fastpower(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fastpower(a * a, n/2)  # a**n = (a**2)**n/2
    elif n % 2 != 0:
        return a * fastpower(a, n - 1)  # a**n = a*a**(n-1)

print(fastpower(float(input()), int(input())))
