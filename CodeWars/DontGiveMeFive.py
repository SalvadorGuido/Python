a = 1
b = 9
c = str(a)
count = 0


def dont_give_me_five(a,b):
    c = str(a)
    count = 0

    for i in range(a, b +1 , 1):
        c = str(c)
        if '5' in c:
            c = int(c)
            c += 1
        else:
            count += 1
            c = int(c)
            c += 1
    return count


print(dont_give_me_five(a, b))

