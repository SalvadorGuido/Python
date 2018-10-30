def breakChocolate(n, m):
    if n <= 0 or m <= 0: return 0
    return n*m - 1


x = int(input())
y = int(input())
print(breakChocolate(x,y))
