def twice(x):
    x = int(x)
    return x/2

def four(a):
    a = int(a)
    return a*4

number1 = twice(27)
print(four(number1))

def string_to_float(x):
    try:
        x = float(x)
        return x
    except ValueError:
        return 'can\'t be float'

print(string_to_float('5.000088855'))
print(string_to_float('453443'))
print(string_to_float('sdfdfjs'))
