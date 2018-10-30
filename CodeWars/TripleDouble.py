def triple_double(a, b):
    a = str(a)
    b = str(b)
    c1 = 1
    c2 = 0
    r1 = a[0]
    r2 = b[0]
    for i in range(0, len(a), 1):
        print(r1, a[i])
        if a[i] == r1:
            r1 = a[i]
            c1 += 1
        else:
            print("else")
            r1 = a[i]
            c1 = 1
        if c1 == 3:
            print('The value is repeated {} times'.format(c1))
            r2 = r1
            break
    for i in range(0, len(b), 1):
        print(r2, b[i])
        if b[i] == r2:
            r2 = b[i]
            c2 += 1
        else:
            print("else")
            r2 = b[i]
            c2 = 1
        if c2 == 2:
            print('The value is repeated {} times'.format(c2))
            break
    print(c1, c2)
    if c1 == 3 and c2 == 2:
        return 1
    else:
        return 0


x = 4592992299777
y = 41177722899

triple_double(x,y)
