def calc(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        try:
            return x / y
        except ZeroDivisionError:
            return f'Error! {y} must be different of zero.'

operation = 'mul'
print(calc(5, 5, operation))