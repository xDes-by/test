# count = int(input("Ведите кол-во элементов в списке: "))
# k = int(input("Исключаем каждый: ")) - 1
#
# elements = list(range(1, count + 1))
#
# index = k
# while len(elements) > 1:
#     del elements[index]
#     index = (index + k) % len(elements)
#
# print("Последний оставшийся элемент:", elements[0])

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
