int()
float()
str()

a = int("123")
# print( int(4.5), 'a =', type(a), a, type("123") )

# print( int("123a" ) ) # выдаёт ошибку
# print( int("2.5") )
# команда int переводит из одного типа в другое

# print( float(23), float("12"), float("12.4"), float("23fd") )

# print( str(12), str(2.5) )

#0123456789101112 индекс
s = "Random string"
# print( s[0], s[5]) # чтение символов

"""
В питоне есть два типа переменных:
  - изменяемые - mutable
  - не изменяемые - immutable
    str
    int
    float
    bool
    None
"""

# s[0] = "b" # error
x = 10 # создали переменную x
x = 11 # пересоздали переменную x с значением 11
# print('x =', x)
# print(s*3, 4*4)

name = "Johnny"
surname = "Depp"
age =  46 #int
# print(name, surname, age)

# print('name', name, 'surname', surname, 'age', age)
# "23" + 23 # ошибка

# print('name ' + name + ' surname ' + surname + ' age ' + str(age))

output = "His name is {}, surname {} and his age {}".format(name, surname, age)
# print (output)

output = "His name is {0}, surname {1} and his age {2}".format(name, surname, age)
# print(output)

output = f"{name:10} {surname:10} {age:10}" 
print(output)

output = f"{name:>10} {surname:>10} {age:>10}" 
print(output)

output = f"{name:<10} {surname:<10} {age:<10}" 
print(output)

output = f"{name:^10} {surname:^10} {age:^10}" 
print(output)

output = f"{name:>15} {surname:>15} {age:>15}" 
print(output)


