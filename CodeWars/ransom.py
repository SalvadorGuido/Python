letter = "quiero respuestas ahora"

magazine = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'qwertyuiopasdfghjklzxcvbnm', 'qwertyuiopasdfghjklzxcvbnm', 'qwertyuiopasdfghjklzxcvbnm', 'qwertyuiopasdfghjklzxcvbnm']

ransom_d = {}
if not ransom_d:
    print('Prueba')

# Fill Dictionary
for c in letter.replace(" ", ""):
    if c in ransom_d:
        ransom_d[c] += 1
    else:
        ransom_d[c] = 1

found = False

for page in magazine:
    for c in page:
        if c in ransom_d and ransom_d[c] > 0:
            ransom_d[c] -= 1
            if all(value == 0 for value in ransom_d.values()):
                print('done')
                found = True
                break
    if found:
        break
