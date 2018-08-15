shopping_list = ["milk", "pasta", "eggs", "spam", "rice"]

for item in shopping_list:
    if item is "spam":
        continue
    print("buy " + item)

print('-'*50)

for item in shopping_list:
    if item is "spam":
        break
    print("buy " + item)

print('-'*50)

meal = ["egg",'bacon','spam', 'sausages']
for item in meal:
    if item is 'spam':
        nasty_food_item = item
        break

if nasty_food_item:
    print("Can't have anything without {} in it".format(nasty_food_item))

print('-'*50)

meal = ["egg", 'bacon', 'tomato', 'sausages']
nasty_food_item1 = ''
for item in meal:
    if item is 'spam':
        nasty_food_item1 = item
        break
else:
    print("I'll have a plate of that then, please")
if nasty_food_item1:
    print("Can't have anything without {} in it".format(nasty_food_item1))

print('-'*50)

