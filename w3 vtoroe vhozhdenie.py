s = input()
pos = s.find('f')
if pos != -1:
    pos = s.find('f', pos + 1)
    print(pos)
else:
    print(-2)
