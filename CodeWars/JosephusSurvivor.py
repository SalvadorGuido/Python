def josephus_survivor(n,k):
    print(n,k)
    c = 1
    a = list(range(1,int(n)+1))
    values = []
    print(a)
    while len(values) < n:
        for item in a:
            if item not in values:
                print(item, c)
                if c == k:
                    print(item)
                    values.append(item)
                    a.remove(item)
                    print(item)
                    c = 1
                else:
                    c += 1
    print(values)
    return values[-1]

x = 11
y = 19

print(josephus_survivor(x,y))