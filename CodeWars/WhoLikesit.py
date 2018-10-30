def likes(n):
    if not n:
        return 'no one likes this'
    else:
        if len(n) == 1:
            return (n[0] + ' likes this')
        if len(n) == 2:
            return(n[0] + ' and ' + n[1] +' like this')
        if len(n) == 3:
            return(n[0] + ', ' + n[1] + ' and ' + n[2] +' like this')
        if len(n) >= 4:
            return(n[0] + ', ' + n[1] + ' and {} others like this'.format(len(n)-2))

x = ['Alex', 'Jacob', 'Mark', 'Max']
print(likes(x))