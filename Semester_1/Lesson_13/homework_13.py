# Задание №1. Написать функцию по нахождению чисел фиббоначи
def fibonacci(n):
    num = 1
    if n > 2:
        num = fibonacci(n-1) + fibonacci(n-2)
    return num

element = input('Введите номер последовательности числа: ')
element = int(element)
value = fibonacci(element)
print(str(element)+' число последовательности равен ' + str(value))


# 2. Написать функцию, которая принимает список строк и из этого списка создает словарь
# где ключами словаря являются значения списка, а значения словаря должны быть None. 
# Не понял задание
def create_dict(keys):
    obj = {}
    for key  in keys:
        obj[key] = None
    
    print(obj)

create_dict(["name", "age", "password"])



# Задание №3. Прочитать про PVM (python virtual machine)
# Прочитал


# Задание №4. Решить эту задачу из кодварса (часть решения я показывал в классе).
# https://www.codewars.com/kata/54d22119beeaaaf663000024/train/python
def shades_of_grey(n):
    shades=[]
    if n < 0:
        return shades
    elif n > 254:
        n =254
    for i in range(n):
        color = f"#{(i+1):02x}{(i+1):02x}{(i+1):02x}"
        shades.append(color)
    return shades
print(shades_of_grey(32))


# Задание №5. Написать функцию, которая создает список внутри списка с 3 столбцами и 4 строками (матрица). 
# Значения внутри списка могут быть любыми.
# Как должен выглядеть ответ: 
# [ 
#     [1, 2, 3], 
#     [1, 2, 3], 
#     [1, 2, 3], 
#     [1, 2, 3], 
# ] 
matrix = []
a, b = 3, 4

for i in range(b):
    arr = []
    for j in range(a):
        arr.append(j)
    matrix.append(arr)

print(matrix)


