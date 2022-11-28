print("Задача №1")
print("Перевернуть строку. phew -> wehp")
print(sep="\n\n")

text = ["phew"]
print('Результат:', text[0][3]+text[0][2]+text[0][1]+text[0][0])
print(sep="\n\n")

print("Задача №2")
print("Прочитать и привести примеры с методами для списков: append, count, copy, insert, sort, extend, pop, index")
print(sep="\n\n")

print('Использование метода append. Метод append() в Python добавляет элемент в конец списка')
rooms = ['Спальня', 'Зал', 'Детская']
print('Список комнат: ', rooms)
rooms.append('Гостинная')
print('Обновлённый список комнат: ', rooms)
print(sep="\n\n")

print('Использование метода count. Метод count() возвращает количество раз, когда указанный элемент появляется в списке')
estimates = ['5', '4', '3', '2', '3', '3', '5', '4', '4']
print('Список оценок: ', estimates)
five = estimates.count('5')
print('Количество пяторок: ', five)
four = estimates.count('4')
print('Количество четвёрок: ', four)
three = estimates.count('3')
print('Количество троек: ', three)
two = estimates.count('2')
print('Количество двоек: ', two)
print(sep="\n\n")

print('Использование метода copy. Метод copy() возвращает мелкую копию списка')
old_numbers = [1, 2, 3, 4, 5]
new_numbers = old_numbers[:]
new_numbers.append(6)
old_numbers = old_numbers.copy()
print('old_numbers:', old_numbers)
print('new_numbers:', new_numbers)
print(sep="\n\n")

print('Использование метода insert. Метод list insert() вставляет элемент в список по указанному индексу')
name = ['my', 'name', 'Oybek']
print('Current text: ', name)
name.insert(2, 'is')
print('Changed text: ', name)
print(sep="\n\n")

print('Использование метода sort. Метод sort() сортирует элементы данного списка в определенном порядке возрастания или убывания')
letters = ['d', 'c', 'b', 'a', 'e']
print('Список букв без сортировки: ', letters)
letters.sort()
print('Отсортированный список букв: ', letters)
print(sep="\n\n")

print('Использование метода extend. Если вам нужно добавить элементы списка в другой список (а не в сам список), используйте метод extend()')
list_methods = ['append', 'count', 'copy', 'insert', 'sort']
print('Методы для списков: ', list_methods)
additional_methods = ['extend', 'pop', 'index']
print('Дополнительный список методов: ', additional_methods)
list_methods.extend(additional_methods)
print('Полный список методов: ', list_methods)
print(sep="\n\n")

print('Использование метода pop. Метод pop() удаляет элемент по заданному индексу из списка и возвращает удаленный элемент')
animals = ['dog', 'cat', 'bear', 'phone', 'sheep']
print('Общий список: ', animals)
animals.pop(3)
print('Список животных: ', animals)
print(sep="\n\n")

print('Использование метода index. Метод index() возвращает индекс указанного элемента в списке')
letters = ['a', 'b', 'c', 'd', 'e']
print('Список букв для поиска индекса: ', letters)
index = letters.index('c')
print('Индекс буквы c: ', index)
index = letters.index('e')
print('Индекс буквы e: ', index)
print(sep="\n\n")
