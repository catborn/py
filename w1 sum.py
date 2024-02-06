digit = int(input())
first = digit // 100
second = (digit // 10) % 10
last = digit % 10
# print(first, '~', second, '~', last)
print(first + second + last)
