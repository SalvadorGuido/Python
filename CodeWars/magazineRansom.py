def createDictionary(message):
    message_list = list(''.join(message.lower().split(' ')))
    for c in message_list:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

def read_pages(magazine):
    for page in magazine:
        for c in page:
            if c in letters:
                if letters[c] == 0:
                    pass
                else:
                    letters[c] -= 1

def is_possible():
    for k,v in letters.items():
        if v != 0:
            return False
    return True

letters = {}
m = "This is a string"
mag= ['apply', 'insgstring', 'string']
message_list = list(''.join(m.split(' ')))
print(message_list)
createDictionary(m)
print(letters)
read_pages(mag)
print(letters)

print(is_possible())

