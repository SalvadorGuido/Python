def is_triangle(a, b, c):
    return (a+b > c) and (a + c > b) and (b +c > a)



a = 4
b = 3
c = 2

print(is_triangle(a,b,c))