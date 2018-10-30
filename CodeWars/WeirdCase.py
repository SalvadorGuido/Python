def to_weird_case(a):

    x = list(a)
    print(x)
    count = 0
    for i in range(0,len(x), 1):
        if count % 2 == 0:
            x[i] = x[i].upper()
        if count %2 == 1:
            x[i] = x[i].lower()
        if x[i] == ' ':
            count = 0
        else:
            count += 1
    s = ''.join(x)
    return s


z = input()
print(to_weird_case(z))

