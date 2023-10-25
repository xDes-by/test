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
shopping_list=[]
shopping_list.append("яблоко")
shopping_list.append("молоко")
shopping_list.append("молоко")
shopping_list.append("хлеб")
shopping_list.append("яйца")
shopping_list.append("сок")
for d in shopping_list:
    print(d)
shopping_list.remove("молоко")
shopping_list[shopping_list.index("яблоко")]= 'банан'
print(shopping_list)
print(len(shopping_list))
input()