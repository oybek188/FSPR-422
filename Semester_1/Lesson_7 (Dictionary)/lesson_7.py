# Интерируемые - interable. Исчесляемый. Это те переменные, которые хранят больше одного значенния

# Dictionary - Словарь
# ключём словаря могут быть только неизменяемые типы переменных

import numbers


user_data = {
    "ключ": "занчение",
    1: None,
    2: 21,
    3: 6.7,
    4: [2,3,4],
    5: (1,2,3),
    6: {"key": "Другой словарь"}
    # [1]: 23, # error
    # (2, 3, [2, 4]): # "Error", # кортеж можно использовать как ключ, но не рекомендуется
}
# print( type(user_data), user_data, user_data["ключ"], sep="\n")

print(sep="\n\n")
# Вывести на экран все значения словаря

# print (type(user_data), user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], sep ="\n")

# print(sep="\n\n")

user_data = {
    "username": "Gobby",
    "password": "szkdjfhlszd",
    "age": 18, # hash ldfskgjzsldvmzcxmv
    "age": 22, # hash ldfskgjzsldvmzcxmv
}
# print(user_data["age"])

user_data_2 = {
    "username": "Gobby",
    "password": "szkdjfhlszd",
    "age": 18, # hash ldfskgjzsldvmzcxmv
    "age": 22, # hash ldfskgjzsldvmzcxmv
}

# user_data = [
#     {
#     "username": "Gobby",
#     "password": "szkdjfhlszd",
#     "age": 18,

#     },
#     {
#     "username": "Gatsby",
#     "password": "ldfkjsldk",
#     "age": 14,
#     }
# ]
# print(user_data[0]["username"], user_data[0]["age"] )

user_data["username"] = "Alabasta"
# print(user_data.keys(), user_data.values(), user_data.items(), sep="\n")

user_list = list(user_data.values())
# print(user_list)

# print( user_data["unexisting"]) # error
# print("get", user_data.get("age"), user_data.get("unexisting"))

# set - множество
# нельзя индексировать
# можно менять через методы и циклы
numbers = {2, 3, 4, "hello", 2, 4}
print(numbers)
numbers = {}
print( type(numbers))
numbers = set()
print( type(numbers))

remove_duplicates = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, "AA", "BB", "AA"]
print( type(remove_duplicates), list(set(remove_duplicates)))
