def last_digit(a, b):

    if a == 1: return a 	# Base cases
    if b == 0: return 1


    temp = int(str(a)[-1]) 	# Create temp value using the last digit of first input
    print(temp)
    while(b>10):			# According to behaviour of powers, each last digit repeats itself every 4 numbers
        b /= 4				# Reducing value of second input to the get it on the first set of powers (1-5)
    print(int(str(temp**int(b + 2))[-1]))
    return int(str(temp**int(b + 2))[-1])


x = 3715290469715693021198967285016729344580685479654510946723
y = 68819615221552997273737174557165657483427362207517952651
#7

print(str(x)[-1])
print(last_digit(x,y))