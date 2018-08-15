a = [2,3,1,5,6]
water = 0
m = max(a)
for i in range(len(a)):
    if a[i+1]:
        if a[i] <= a[i+1]:
            continue
        if a[i] == m:
            continue
        j = i+1
        while a[i] < a[j]:
            water += a[i] - a[j]
            j += 1
        i = j
