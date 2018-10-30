atoms = {}

#
# def parse_molecule(formula):
#     s = ''
#     initial_index = 0
#     inside_parentesis = 0
#     for i in range(0,len(formula)):
#         s += formula[i]
#         if formula[i] == '[':
#             initial_index = i
#         while formula[i] != ']':
#             inside_parentesis += 1
#         s += formula[initial_index:inside_parentesis] * int(formula[i+1])
#     return s

def multiply_tuple(t):
    m = ''
    m = t[0] * t[-1]
    return m

def inside_parentesis(f):
    try:
        start = f.index('(') + len('(')
        end = f.index(')')
        return (f[start:end],int(f[end+1]))
    except ValueError:
        return ""

def inside_square(f):
    try:
        start = f.index('[') + len('[')
        end = f.index(']')
        return (f[start:end],int(f[end+1]))
    except ValueError:
        return ""

water = 'H2O'
formula1 = 'Mg(OH)2'
formula = 'K4[ON(SO3)2]2'

# print(parse_molecule(magnesium_hydroxide))

# t = eval(formula)
# print(t)
a = list(formula)
print(a)
b = []
for i in range(len(formula)):
    if i < len(formula)-1:
        # print('='*40)
        # print(formula[i])
        # print(ord(formula[i]))
        # print(formula[i+1])
        # print(ord(formula[i+1]))
        # print(ord(formula[i]) + ord(formula[i+1]))
        if 212 > ord(formula[i]) + ord(formula[i+1]) > 162:
            print('='*40)
            print('Entra')
            a.append(formula[i]+formula[i+1])
            b.append(formula[i]+formula[i+1])
        elif 91 > ord(formula[i]) > 64:
            b.append(formula[i])
    print(formula[i])
print(b)



# for i in range(0,len(formula),1):
#     s += formula[i]
#     if formula[i] == '[':
#         initial_index = i
#     while formula[i] != ']':
#         inside_parentesis += 1
# s += formula[initial_index:inside_parentesis] * int(formula[i+1])

print(multiply_tuple(('OH', 2)))
print(inside_parentesis(formula))
print(multiply_tuple(inside_parentesis(formula)))
print(inside_square(formula))
print(multiply_tuple(inside_square(formula)))

for i in range(inside_square(formula)[1]):
    print(inside_parentesis(multiply_tuple(inside_square(formula))))




