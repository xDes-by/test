print('calculator')
a = int(input('Введите число'))
b = int(input('Введите число'))
c = input('Введите символ + - * ** / // %')
if c == '+':
    print('a', '+', 'b', '=', a + b)
if c == '-':
    print('a', '-', 'b', '=', a - b)
if c == '*':
    print('a', '*', 'b', '=', a * b)
if c == '**':
    print('a', '**', 'b', '=', a ** b)
if c == '/':
    print('a', '/', 'b', '=', a / b)
if c == '//':
    print('a', '//', 'b', '=', a // b)
if c == '%':
    print('a', '%', 'b', '=', a % b)