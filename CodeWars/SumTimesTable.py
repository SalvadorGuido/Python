def sum_times_tables(table,a,b):
    s = 0
    for item in table:
        for i in range(a,b+1,1):
            s += item*i
    return s

x = input()
y = 1
z = 10

