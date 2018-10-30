
def multi(a):
    sum = 0
    a = int(a)
    for i in range(0, a):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

x = int(input())

print(multi(x))