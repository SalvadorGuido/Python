def find_short(s):
    a = s.split(' ')
    l = len(a[0])
    for item in a:
        if len(item) < l:
            l = len(item)
    return l # l: shortest word length

x = input()
print(find_short(x))