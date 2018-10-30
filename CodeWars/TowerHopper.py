def is_hoppable(towers):
    current = 0
    while True:
        print('Vuelta')
        if current >= len(towers):
            print('Saliste')
            return True
        if towers[current] == 0:
            print('Estancado')
            return False
        current = next_step(current,towers)


def next_step(pos, towers):
    max_index = 0
    for i in range(pos+1, towers[pos]+1):
        if pos + towers[i] > max_index:
            max_index = towers[pos] + towers[i]
            print(max_index)
    print(max_index)
    return max_index


tow = [1,4,0,0,2,0]

print(is_hoppable(tow))
