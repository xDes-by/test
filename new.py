a = float(input("Введите первое число: "))
operation = input("Выберите операцию (+, -, *, /): ")
b = float(input("Введите второе число: "))

if operation == '+':
    result = a + b
    print("Результат:", result)
elif operation == '-':
    result = a - b
    print("Результат:", result)
elif operation == '*':
    result = a * b
    print("Результат:", result)
elif operation == '/':
    if b != 0:
        result = a / b
        print("Результат:", result)
    else:
        print("Делить на ноль нельзя")
else:
    print("Нет.")