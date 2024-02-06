n = float(input())
sum = 0
sch = 1
while sch <= n:
    sum = sum + (1/(sch**2))
    sch += 1
print(sum)
