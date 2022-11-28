from curses import initscr


print("Задание №1")
print("Прочитать и попробовать методы множеств (set): union, update, add, pop, remove, copy, clear, difference")
print(sep="\n\n")

a = {"яблоки", "груша", "банан"}
b = {"виноград", "яблоки", "персик"}
c = {"гранат", "банан", "апельсин"}
d = {"авокадо", "ананас", "бергамот"}
e = {"авокадо", "грейпфрут", "киви"}
f = {"лайм", "лимон", "локва"}
g = {"манго", "дыня", "нектарин"}
h = {"мандарин", "папайя", "хурма"}
i = {"слива", "мандарин", "айва"}

print("Python Set union() Method")
# Метод union()возвращает набор, содержащий все элементы из исходного набора и все элементы из указанных наборов.
# Вы можете указать столько наборов, сколько хотите, разделив их запятыми.
# Это не обязательно должен быть набор, это может быть любой итерируемый объект.
# Если предмет присутствует более чем в одном наборе, результат будет содержать только один вид этого предмета.
fruits = a.union(b, c)
print("union method:", fruits)

print(sep="\n\n")

print("Python Set update() Method")
# Метод update()обновляет текущий набор, добавляя элементы из другого набора (или любого другого итерируемого).
# Если предмет присутствует в обоих наборах, в обновленном наборе будет присутствовать только один вид этого предмета.
d.update(e)
print("update method:", e)
# Тут я не понял, почему ответ выдал только 3 элемента вместо 5 ?

print(sep="\n\n")

print("Python Set add() Method")
# Метод add()добавляет элемент в множество.
# Если элемент уже существует, add()метод не добавляет элемент.
a.add("клюква")
print("add method 1:", a)
b.add("персик")
print("add method 2:", b)

print(sep="\n\n")

print("Python Set pop() Method")
# Метод pop()удаляет случайный элемент из набора.
# Этот метод возвращает удаленный элемент.
c.pop()
print("pop method 1:", c)
j = c.pop()
print("pop method 2:", j) # Вернуть удаленный элемент
# В мануале было сказано что 'pop method 2' вернёт удалённый элемент, но он просто выдал рандомный элемент из набора. Почему?

print(sep="\n\n")

print("Python Set remove() Method")
# Метод remove()удаляет указанный элемент из набора.
# Этот метод отличается от discard()метода тем, что remove() метод вызовет ошибку , если указанный элемент не существует, а discard()метод не будет .
d.remove("ананас")
print("remove method:", d)

print(sep="\n\n")

print("Python Set copy() Method")
# Метод copy()копирует набор
k = f.copy()
print("copy method:", k)

print(sep="\n\n")

print("Python Set clear() Method")
# Метод clear()удаляет все элементы в наборе
g.clear()
print("clear method:", g)

print(sep="\n\n")

print("Python Set difference() Method")
# Метод difference()возвращает набор, содержащий разницу между двумя наборами.
# Значение: возвращаемый набор содержит элементы, которые существуют только в первом наборе, а не в обоих наборах.
l = h.difference(i)
print("difference method:", l)
