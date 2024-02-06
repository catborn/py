from math import sqrt


def isPrime(n):
    i = 2
    while n % i != 0 or i == n:
        i = i + 1
        if i > sqrt(n):
            return n


n = int(input())
if isPrime(n):
    print('YES')
else:
    print('NO')
