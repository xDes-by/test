# num1 = int(input("Введите первое число: "))
# sing = input("Операция: ")
# num2 = int(input("Введите второе число: "))
#
# if sing == "+":
#     print(num1+num2)
# elif sing == "-":
#     print(num1-num2)

# expression = input("Введите выражение (например, '5+9' или '5/9' или '5*9'): ")
#
# if '+' in expression:
#     operator = '+'
# elif '-' in expression:
#     operator = '-'
# elif '*' in expression:
#     operator = '*'
# elif '/' in expression:
#     operator = '/'
# else:
#     print("Неверный формат выражения")
#     exit()
#
# operands = expression.split(operator)
# print(operands)
#
# operand1 = float(operands[0])
# operand2 = float(operands[1])
#
# if operator == '+':
#     result = operand1 + operand2
# elif operator == '-':
#     result = operand1 - operand2
# elif operator == '*':
#     result = operand1 * operand2
# elif operator == '/':
#     if operand2 == 0:
#         print("Деление на ноль недопустимо")
#         exit()
#     result = operand1 / operand2
#
# print("Результат:", result)


import datetime

# Получить текущую дату
current_date = datetime.date.today()

# Извлечь номер месяца из текущей даты (1 - январь, 2 - февраль, и так далее)
month_number = current_date.month

print("Текущий месяц:", month_number)