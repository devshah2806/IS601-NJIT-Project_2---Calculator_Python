def division(a, b):
    a = int(a)
    b = int(b)
    if b != 0:
        c = b / a
        return round(c, 9)
    else:
        return print('Denominator cannot be Zero')
