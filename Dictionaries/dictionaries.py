fruit = {"orange": 'a sweet, orange, citrus fruit',
         "apple": 'good for making sider',
         "lemon": 'a sour, yellow citrus fruit',
         'grape': 'a small, sweet fruit growing in bunches',
         'lime': 'a sour, green citrus fruit'}

print(fruit)
print('-'*40)
print(fruit.keys())
print('-'*40)
print(fruit.values())
print('-'*40)
for k,v in fruit.items():
    print(v)
print('-'*40)
print(fruit['lemon'])
print('-'*40)
fruit['pear'] = "an odd shaped apple"
print(fruit)
print('-'*40)
del fruit['lemon']
print(fruit)
print('-'*40)
# fruit.clear()
# print(fruit)
while True:
    dic_key = input('Please enter a fruit: ')
    if dic_key == 'quit':
        break
    if dic_key in fruit:
        description = fruit.get(dic_key)
        print(description)
    else:
        print("Don't have a {}".format(dic_key))
print(fruit)