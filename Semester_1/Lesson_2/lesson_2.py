"""
Базовые типы данных:
  int - целые числа
  float - дробные числа
  str - строки
  bool - правда/ложь
  None - ничего
Операции с числами: + - * / // ** %
"""
# # функция
# print((1 + 6)/2) # float
# print( 6//2 ) #int

# print( 2 ** 4 )
# print( 13 % 6 )
# print( 12 % 6 )
# значение
12
3.5
# переменная
a = 12
b = 3
# print(a)
# выражения
c = a + b
# print (c)

c = c + 2
c += 2
# print(c)
c *= 2
# print (c)
c /= 2
# print (c)
c //= 2
# print (c)

import math
print(abs(-12))
print( math.sqrt(16), math.sqrt(25), 4.5, 54)
print( math.sqrt(16), math.sqrt(25), 4.5, 54, sep="\n")
print( math.sqrt(16), math.sqrt(25), 4.5, 54, sep="\t")

#Создание строк
s_1 = (
  'Hello'
  " Hello 4"
  " Hello 4"
)
s_2 = "Hello\n" \
      "Hello 3" \
      "Hello 3"
s_3 = """
Hello
Hello 2
"""
# print(s_1, s_2, s_3, sep="\n\n")
s_1 = "hello"
s_2 = "world"
s_3 = s_1 + " " + s_2 + "!"
# print(s_3, 2 + 3)

#Полиморфизм - одна команда/интерфейс которая работает с разными типами данных по разному
# CamelCase
# nameSurenameFamily
