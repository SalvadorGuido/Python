def last_digit(a, b):
    u = a
    print(u)
    o = b
    print(o)
    c = str((u**o)%10)
    return int(c[-1])

x = 3715290469715693021198967285016729344580685479654510946723
y = 68819615221552997273737174557165657483427362207517952651
#7
print(last_digit(x,y))