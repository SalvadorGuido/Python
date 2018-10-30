def summationOfPrimes(n):
    s = 0
    primes = []
    for num in range (2,n+1):
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    for i in range(0,len(primes),1):
        s += primes[i]
    return s


a = int(input())

print(summationOfPrimes(a))