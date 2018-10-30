a = 'a'
print(ord(a))
print(chr(ord(a) - 32))

a = input()

b = []
c = []
b = a.split(' ')

for item in b:
    if 64 < ord(item[0]) < 91 or 47 < ord(item[0]) < 58:
        c.append(item)
    else:
        c.append(chr(ord(item[0]) - 32) + item[1:])

s = ' '.join(map(str,c))
print(s)