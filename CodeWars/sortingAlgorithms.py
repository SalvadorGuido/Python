import random
size = random.randrange(50)
a = []

# Creating random list
for i in range(size):
    a.append(random.randrange(172))

print(a)

# Bubble Sort

def bubble(a):
    switch = 1
    run = 0
    for run in range(size):
        if switch == 1:
            switch = 0
            for i in range(size-run-1):
                if a[i] > a[i+1]:
                    aux = a[i]
                    a[i] = a[i+1]
                    a[i+1] = aux
                    switch = 1
    return a,run
print("Arranged list: {}\nNumber of Runs: {}".format(bubble(a)[0], bubble(a)[1]))


print(a)
