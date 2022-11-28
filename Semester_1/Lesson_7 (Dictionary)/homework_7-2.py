print("Задание №2")
print("Прочитать и попробовать методы словарей (dict)")
print(sep="\n\n")

print("Python Dictionary clear() Method")
# Метод clear()удаляет все элементы из словаря
user = {
  "name": "Oybek",
  "surname": "Kasymov",
  "age": 35
}
user.clear()
print("clear method:", user)

print(sep="\n\n")

print("Python Dictionary copy() Method")
# Метод copy()возвращает копию указанного словаря
user = {
  "name": "Oybek",
  "surname": "Kasymov",
  "age": 35
}
user.copy()
print("copy method:", user)

print(sep="\n\n")

print("Python Dictionary fromkeys() Method")
# Метод fromkeys()возвращает словарь с указанными ключами и указанным значением
a = ('secret1', 'secret2', 'secret3')
b = 0
key = dict.fromkeys(a, b)
print("fromkeys method:", key)

print(sep="\n\n")

print("Python Dictionary get() Method")
# Метод get()возвращает значение элемента с указанным ключом
user = {
  "name": "Oybek",
  "surname": "Kasymov",
  "age": 35
}
a = user.get("surname")
print("get method 1:", a)
b = user.get("year", 1987)
print("get method 2:", b)

print(sep="\n\n")

print("Python Dictionary items() Method")
# Метод items()возвращает объект представления. Объект представления содержит пары ключ-значение словаря в виде кортежей в списке.
# Объект представления будет отражать любые изменения, внесенные в словарь.
user = {
  "name": "Oybek",
  "surname": "Kasymov",
  "age": 35
}
a = user.items()  # Вернуть пары ключ-значение словаря
print("items method 1:", a)
user["age"] = 36 # Когда элемент в словаре изменяет значение, объект представления также обновляется
print("items method 2:", a)

print(sep="\n\n")

print("Python Dictionary keys() Method")
# Метод keys()возвращает объект представления. Объект представления содержит ключи словаря в виде списка.
# Объект представления будет отражать любые изменения, внесенные в словарь
a = user.keys() # Вернуть ключи
print("keys method 1:", a)
user["year"] = "1987" # Когда элемент добавляется в словарь, объект представления также обновляется
print("keys method 2:", a)

print(sep="\n\n")

print("Python Dictionary pop() Method")
# Метод pop()удаляет указанный элемент из словаря.
# Значение удаленного элемента является возвращаемым значением pop() метода
user.pop("surname") # Удалить «surname» из словаря
print("pop method 1:", a)
a = user.pop("name") # Значение удаленного элемента — это возвращаемое значение метода pop()
print("pop method 2:", a)

print(sep="\n\n")

print("Python Dictionary popitem() Method")
# Метод popitem()удаляет элемент, который последним был вставлен в словарь. В версиях до 3.7 popitem()метод удаляет случайный элемент.
# Удаленный элемент — это возвращаемое значение popitem() метода в виде кортежа
user = {
  "name": "Oybek",
  "surname": "Kasymov",
  "age": 35
}
user.popitem() # Удалить последний элемент из словаря
print("popitem method 1:", user)

user = {
  "name": "Oybek",
  "surname": "Kasymov",
  "age": 35
}
a = user.popitem() # Удаленный элемент является возвращаемым значением метода pop()
print("popitem method 2:", a)

print(sep="\n\n")

print("Python Dictionary setdefault() Method")
# Метод setdefault()возвращает значение элемента с указанным ключом.
# Если ключ не существует, вставьте ключ с указанным значением
user = {
  "name": "Oybek",
  "surname": "Kasymov",
  "age": 35
}
x = user.setdefault("surname", "Фамилия") # Получите значение элемента «surname»
print("setdefault method 1:", x)
y = user.setdefault("year", "1987") # Получить значение элемента «year», если элемента «year» не существует, вставить «year» со значением «1987»
print("setdefault method 2:", y)

print(sep="\n\n")

print("Python Dictionary update() Method")
# Метод update()вставляет указанные элементы в словарь.
# Указанные элементы могут быть словарем или итерируемым объектом с парами ключ-значение
user.update({"year": "1987"})
print("update method:", user) # Вставьте элемент в словарь

print(sep="\n\n")

print("Python Dictionary values() Method")
# Метод values()возвращает объект представления. Объект представления содержит значения словаря в виде списка.
# Объект представления будет отражать любые изменения, внесенные в словарь
user = {
  "name": "Oybek",
  "surname": "Kasymov",
  "age": 35
}
x = user.values()
print("values method 1:", x) # Вернуть значения
user["year"] = "1987"
print("values method 2:", x) # Когда значения изменяются в словаре, объект представления также обновляется
