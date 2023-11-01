# N = int(input("Введите число N: "))
# k = int(input("Введите число k: ")) - 1
#
# array = list(range(1, N + 1))
# index = 0
# while len(array) > 1:
#     index = (index + k) % len(array)
#     del array[index]
#
# print("Last:", array)

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
