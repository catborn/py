now = int(input())
max = 0
kol = 0
while now != 0:
    if now > max:
        max = now
        kol = 1
    elif now == max:
        max = now
        kol = kol + 1
    now = int(input())
print(kol)
