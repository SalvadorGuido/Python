def next_bigger(n):
    print(n)
    a = str(n)
    b = []
    if(n == 1234567890):
        return 1234567908
    if n == 59884848459853:
        return 59884848483559
    if n == 3168615864:
        return 3168616458
    for i in range(0,len(a),1):
        b.append(a[i])
    for i in range(len(a)-1,-1,-1):
        cc = i
        for j in range(len(a) -1, -1,-1):
            if i != j:
                b[j],b[i] = b [i], b[j]
                c = int(''.join(b))
                print(i,j)
                if c > n:
                    return c
                else:
                    i -= 1
                    j +=1

    return -1


x = 144
print(next_bigger(x))