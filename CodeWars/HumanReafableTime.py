def make_readable(s):
    sec = int(s)
    if sec > 59:
        m = int(sec/60)
        sec -= m*60
        if m > 59:
            hr = int(m/60)
            m -= hr*60
        else:
            hr = 0
    else:
        m = 0
    return "{:02}:{:02}:{:02}".format(hr, m, sec)


x = 359999
print(make_readable(3661))