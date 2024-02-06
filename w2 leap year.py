year = int(input())
leap1 = year / 4
leap11 = year // 4
leap2 = year / 100
leap22 = year // 100
leap3 = year / 400
leap33 = year // 400
# print(leap1)
# print(leap2)
# print(leap11)
# print(leap22)
if leap1 == leap11 and leap2 != leap22 or leap3 == leap33:
    print('YES')
else:
    print('NO')
