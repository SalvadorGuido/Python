
def persistence(a):
    count = 0
    a = int(a)
    if a < 10:
        return count
    else:
        count += 1
        # print(count)
        a = str(a)
        r = len(a)
        b = []
        res = 1
        for i in range(0,r,1):
            b.append(int(a[i]))
        # print(b)

        for item in b:
            res *= item
        # print(res)
        count += persistence(res)
    return count

x = input()

print(persistence(x))