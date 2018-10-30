def binary_array_to_number(s):

    for i in range(0, len(s),1):
        s[i] = str(s[i])

    print(s)

    a = ''.join(s)
    print(a)
    b = int(a, 2)
    return b


print(binary_array_to_number([1,1,1,1]))