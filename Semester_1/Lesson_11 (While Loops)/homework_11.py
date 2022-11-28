# Имея список чисел, удалить дупликаты из этого списка и создать новый 
# [1, 1, 2, 3, 4, 4, 5, 3] -> [1, 2, 3, 4, 5]
list = [1, 1, 2, 3, 4, 4, 5, 3]
print('Оригинальный список:', list)
list2 = set(list)
print('Без дубликатов:', list2)

print(sep="\n")
# Создать программу, которая сортирует словарь по ключу и возвращает в ответ список из кортежей 
sort_dict = ({3:"hello", 2:"hello", 1:"hello"}) # == [(1,"hello"), (2,"hello"), (3,"hello")]
print('Оригинальный словарь:', sort_dict)
print('Отсортированный словарь:', sorted(sort_dict.items()))

print(sep="\n")
# Задание №1
#  Используя цикл вывести на экран дерево 
#     * 
#    *** 
#   *****
#  *******
#     * 
#     *
x = 5
for i in range(x):
    print(' ' * (x-i-1) + '*' * (i*2+1))
print(' ' * (x-2), '*')
print(' ' * (x-2), '*')

print(sep="\n")
# Задание №2
# Найти четные и нечетные числа в списке и вывести на экран сообщение что они четные или нечетные. 
nums = [2, 3, 4, 5, 6] # четные - 2 4 6 # нечетные - 3 5 
for i in range(len(nums)):
    print(nums[i], "нечетное" if i & 1 else "четное", sep="=")

print(sep="\n")
# Задание №3
# Переписать код переводу списка чисел из фарангейт в цельсий через while цикл (homework_10-2).
faranheits = [20, 19, 24, 45, 140]
i = 0
while i < len(faranheits):
    celsius = ((faranheits[i]) - 32) * 5 / 9
    i += 1
    if celsius >= 50:
        print(f"Слишком горячо: {celsius}")
        break
    elif celsius <= 5:
        print(f"Жить можно: {celsius}")

print(sep="\n")
# Задание №4
# Переписать код по рисованию квадрата через while цикл (lesson_11).
square_line = 4
i = -1
star = "*"
while i < square_line -1: 
    i += 1
    # print(i)
    if i > 0 and i < (square_line -1):
        empty_space = " " * (square_line -2)
        print(f"{star}{empty_space}{star}")
    else:
        print(star * square_line)

print(sep="\n")
