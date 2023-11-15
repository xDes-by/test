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

people = int(input('количество человек:'))
c = int(input('число в считалке:'))
print(' каждый выбывает', c, 'человек')
a = [i for i in range(1, people+1)]
start = 0
while len (a)>1:
    print('людей:', a)
    print('начало счета', a[start])
    delete = (start+c-1)%len(a)
    if a[delete] == a[-1]:
        start = 0
    else:
        start = delete
    print('номер человека', a.pop(delete))
    print('остался', a[0])