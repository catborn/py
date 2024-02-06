now = int(input())
kol = 0
while now != 0:
    if now % 2 == 0:
        kol = kol + 1
    now = int(input())
print(kol)
