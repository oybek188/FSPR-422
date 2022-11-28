# Матрица
from distutils.log import error


[2,3,4,5,6,7] # вектор
matrix = [[2,3,4], [5,6,7]] # матрица 3 столбца и 2 строки
# 2   3   4
# 5   6   7
# random = list(1) # error
# random = list(True) # error

random = list("Random %^&(&(*)") # error
splitted_string = "Split me ! random".split("me ! ") # ' '
print(random, splitted_string, ''.join(random),sep="\n")

# Tuple - кортеж (interable)
numbers = (2,3,4,5,6)
print(numbers, numbers[3])
            # 0       1   2       3
numbers = ((4.5), 4.5, "fafa", [5,6,7])
print(numbers, numbers[3])

# number[1] = "changed"
# читать, создавать
numbers = (2, 3, 5, [4, 5])
numbers[3][0] = 24
print(numbers[3], numbers[3][0])

#           0         1    2  3  4
numbers = [[2,3,4], [5,6], 5, 6, 7]
numbers[0][2]

numbers = (2, 3, 4)
print('1', type(numbers), numbers)
numbers = tuple()
print(type(numbers), numbers)
numbers = ()
print(type(numbers), numbers)
numbers = 5, 3, 1
print('last', type(numbers), numbers)

a = [2,3,5]
a = tuple(a)
print(type(a), a)
a = tuple("Hello")
print(type(a), a)
