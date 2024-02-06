now = int(input())
max = 0
kolnow = 0
kol = 1
while now != 0:
    if now == max:
        max = now
        kolnow = kolnow + 1
        if kolnow > kol:
            kol = kolnow
    elif now != max:
        max = now
        kolnow = 1
    now = int(input())
print(kol)
