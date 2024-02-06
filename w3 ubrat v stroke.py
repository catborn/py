s = str(input())
sob = s[::-1]
h1 = s.find('h')
h2 = sob.find('h')
l2 = len(s) - h2
print(s[0:h1] + s[l2:])
