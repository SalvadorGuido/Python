def split2(a):
    b = []
    count = 0
    s = ''
    r = len(a)
    if r % 2 == 1:
        a += "_"
    for item in a:
        if count == 0 or count == 2:
            count = 0
            count += 1
            s = item
        else:
            count += 1
            s += item
            b.append(s)
    return b

x = input()
print(split2(x))
