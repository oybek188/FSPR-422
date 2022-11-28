# bool
# True | False
# Любое число что не ноль - это правда (True)
# Если переменная пустая - то она ложь (False)

# True=1 False=0

# print(False + 3)
# x = 10
# y = 20
# if x > y:
#     print(True)
# else:
#     print(False)

"name surname".split() # ['name', 'surname']
# a if condition (значение) else b
# print( True if x > y else False)

# ==, !=, >, >=, <, <=, is, is not, in, not in, not, and, or

# [] {} () "" 0 # это всё False

# if []: # True
#     print(True)

# if -19: # True
#     print(True)

name = "Oybek"
skill = "D2"
age = 35
surname = "Kasymov"

# if name == "Oybek" and skill == "D2": # Обязатель нужно полное соответствие
#     print(name, skill)
# else:
#     print("And")

# if name == "Sardor" or skill == "D2": # Должно соответствовать то или другое
#     print(name, skill)
# else:
#     print("Or")

# if not age: # Not отрицает True и возвращает False
#     print(age) 
# else:
#     print("Age is false")

#               True                     True
#       True              True
# if (name == "Oybek" and age > 30) or skill == "D2":
#     print(name, age, skill)
# else:
#     print("Invalid name, age, skill")

# if (name == "Oybek" or age > 36) or skill == "D2":
#     print(name, age, skill, "second output")
# else:
#     print("Invalid name, age, skill")

# is, ==
# is - сравнивает id двух значений
# == - сравнивает значения
# id()
a = 1
b = 1
print( id(a), id(b) )

t_1 = ()
t_2 = ()
print( id(t_1), id(t_2))
print( t_1 == t_2)
print( "tuple", t_1 is t_2) # False
print("1 ==1", 1 == 1, 1 is 1)

# Изменяемые типы данных
# [] []
l_1 = [1, 2] # 1234567
l_2 = [1, 2] # 7891234
print(l_1 == l_2)
print(l_1 is l_2)

d_1 = {1: 1}
d_2 = {1: 1}
print("dict", d_1 == d_2)
print("dict", d_1 is d_2)

print( l_1, id(l_1), l_2, id(l_2))
l_1.append(4)
print( l_1, id(l_1), l_2, id(l_2))


# isinstance
name = 12
print(isinstance(name, str))
print(isinstance(name, (str, int))) 

