def reverse_words(s):
    r = len(s)
    a = []
    for i in range(r-1,-1, -1):
        a.append(s[i])
        #print(i)
    b = ''.join(map(str,a))
    print(b)
    c = b.split(' ')
    print(c)
    c = c[::-1]
    print(c)
    b = ' '.join(map(str,c))
    return b

x = 'Luis me la pela.'

print(reverse_words(x))