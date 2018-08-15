a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
steps = 0

def bs(l,value, start, end):
    half = (start + end) // 2
    global steps
    if start > end:
        return -1
    if value == l[half]:
        steps += 1
        return half
    elif value < l[half]:
        steps += 1
        return bs(l,value,start,half-1)
    elif value > half:
        steps += 1
        return bs(l,value, half+1, end)
    return -1

print("The value is found in index: {}".format(bs(a,13,1,20)))
print("The amount of steps to find the variable is: {}".format(steps))