n = int(input())
i = 0
sum = 0
while i <= n:
    sum = sum + i ** 2
    i = i + 1
    if n <= 0:  # не нужно наверное
        continue# не нужно наверное
print(sum)
