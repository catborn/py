now = int(input())
nowMax = 0
secMax = 0
while now != 0:
    if now >= nowMax:
        secMax = nowMax
        nowMax = now
    elif now >= secMax:
        secMax = now
    now = int(input())
print(secMax)
