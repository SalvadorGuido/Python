
def distance(point1, point2):
    suma = pow(point2[0]-point1[0],2) + pow(point2[1]-point1[1],2)
    return pow(suma,0.5)

def Position(a):
    return a[2]

def create_tuple_distance(points):
    tup = ()
    origin = (0, 0)
    for point in points:
        tup += (point + (distance(point, origin),),)
        print(point)
    # tup = list(tup)
    print(sorted(tup,key = Position))

    return sorted(tup,key = Position)

def closest_point(points, k):
    for i in range(k):
        print(points[i][:2])

p = ((1,2),(-5,2),(2,3))


distances = ()
print(p)

print(create_tuple_distance(p))

closest_point(create_tuple_distance(p),1)