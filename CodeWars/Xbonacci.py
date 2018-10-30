def Xbonacci(a,n):
    b = list(a)
    c = []
    if n < len(a):
        return a[:n]
    for i in range(0,n-len(a),1):
        print("Entra al for")
        c.append(sum(b))
        b.append(sum(b))
        b.pop(0)
        print(b)
    return a + c


x = [1,2,3,0]
y = 10
print(Xbonacci(x,y))

print(sum(x))
