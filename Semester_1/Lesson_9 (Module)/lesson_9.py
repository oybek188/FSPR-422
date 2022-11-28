# b = [2, 3, 4]
# b.append(23) # [2, 3, 4, 23]
# a = [2, 3, 4]

# # a это b, b это a
# a = [2, 3, 4]
# b = b.append(43)
# print("a=", a, "b=", b)

# # с копированием
# a = [2, 3, 4]
# b = a.copy()
# b.append(43)
# print("a=", a, "b=", b)

# # с копированием
# a = [2, 3, 4, [2, 3]]
# b = a.copy()
# b[2] = 400
# b[3][1] = 12
# print("a=", a, "b=", b)

# # Модуль для глубокого копирования
# import copy
# # import numbers

# a = [2, 3, 4, [2, 3]]
# b = copy.deepcopy(a)
# b[2] = 400
# b[3][1] = 12
# print("a=", a, "b=", b)

print("list")
numbers = [1, 2, 3, 4, 5, 6, 7]
for num in numbers:
    print(num + 2)
print(sep="\n")

print("tuple")
numbers = (1, 2, 3, 4, 5, 6, 7)
for num in numbers:
    print(num + 2)
print(sep="\n")

print("set")
numbers = {1, 2, 3, 4, 5, 6, 7}
for num in numbers:
    print(num + 2)
print(sep="\n")

print("dict")
user = {
    "name": "George",
    "age": 25,
    "skill": "swim",
}
for key in user:
    print(key)
print(sep="\n")

print("dict vals")
for val in user.values():
    print(val)
print(sep="\n")

print("dict items")
for key, val in user.items():
    print("key =", key, "val =", val)
