def top_3_words(text):
    freq = {}
    word = ''
    for c in text:
        if c == "'" and len(word) < 2:
            word = ''
            continue
        if c != ' ' and c not in "!@#$%^&*()_+=[]{};,./:<>?|":
            word += c.lower()
        if c == ' ' and word != '':
            if word in freq:
                freq[word] += 1
                # print(freq[word])
            else:
                freq[word] = 1
                # print(freq[word])
            if word[-1] == text[-1]:
                if word in freq:
                    freq[word] += 1
                    # print(freq[word])
                else:
                    freq[word] = 1
                    # print(freq[word])
            word = ""
    #     print(word)
    # print(freq)
    a = []
    if len(freq) >= 3:
        for i in range(3):
            m = max(freq, key=freq.get)
            a.append(m)
            del freq[m]
        # print(a)
        return a
    else:
        for i in range(len(freq)):
            m = max(freq, key=freq.get)
            a.append(m)
            del freq[m]
        # print(a)
        return a

print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))
