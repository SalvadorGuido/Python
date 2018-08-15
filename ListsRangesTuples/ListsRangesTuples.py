menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['egg', 'spam', 'bacon'])

print(menu)


print('-'*50)
for meal in menu:
    if not "spam" in meal:
        print(meal)
        for food in meal:
            print(food)