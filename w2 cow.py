cow = int(input())
if cow == 11 or cow == 12 or cow == 13 or cow == 14:
    print(cow, 'korov')
elif cow == 2 or cow == 3 or cow == 4:
    print(cow, 'korovy')
elif cow == 1 or cow % 10 == 1:
    print(cow, 'korova')
elif cow % 10 == 2 or cow % 10 == 3 or cow % 10 == 4:
    print(cow, 'korovy')
else:
    print(cow, 'korov')
