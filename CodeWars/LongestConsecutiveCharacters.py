
# Mejorar código para que sólo use un diccionario
def longest(input_string):
    consecutive = {}
    streaks = {}
    streak = True

    for i in range(len(input_string)):
        if input_string[i] in consecutive and streak:
            consecutive[input_string[i]] += 1
        elif input_string[i] not in consecutive:
            consecutive[input_string[i]] = 1
            streaks[input_string[i]] = 1
        if consecutive[input_string[i]] > streaks[input_string[i]]:
            streaks[input_string[i]] = consecutive[input_string[i]]
        if input_string[i] in consecutive and not streak:
            consecutive[input_string[i]] = 1
            streak = True
        if i < len(input_string)-1:
            if input_string[i+1] != input_string[i]:
                streak = False

    return {max(streaks, key=streaks.get),max(streaks.values())}


def longest1(input_string):
    count = 0
    max_count = 0
    max_char = ''
    previous_char = ''

    for c in input_string:
        if previous_char == c:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_char = c
        previous_char = c
    return {max_char:max_count}


s = 'aaaabfddddduuuya'

print(longest(s))
print(longest1(s))