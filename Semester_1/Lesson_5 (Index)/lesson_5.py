"""
Можете сами почитать про: 
    complex 
    Decimal 
    Fraction 
 
Изменяемые 
    set - множество 
    dict - словарь 
    list - список 
 
Неизменяемые 
    bin 
    frozenset - множество 
    tuple - кортеж 
    int 
    float 
    str 
    bool 
    None
"""

#012345
"sdfsdf"
names = []
print(names)
names = (list)
print(names)

#        0  1  2  3  4  5   6       7     8     9
names = [1, 2, 3, 4, 5, 6 ,12.5, "ABCD", True, None]

print(names)
names[0] = False
# names[7] = "Name"
print(names[7][0]) # ABCD -> A
#           0               1               2
names = [[2, 3, 4], [4.5, 5.6, 6.6], ['go', 'go1', 'go2']]  # вывести на экран строку 'go2'
print(names[2][2])

# Нарезка (слайсы) - Slice
# интерировать - проходиться по элементам интнрируемых (эти такие переменные, которые могут хранить больше одного значения)

#          0  1  2   3   4   5  6  
numbers = [4, 5, 6, 10, 22, 55, 500]
#         -7 -6 -5  -4  -3  -2 -1

# [начало:конец]
print( "шаг1", numbers[:6:2] ) # 0 + 2 -> 2 + 2 -> 4 -> 6
print( "шаг2", numbers[:6] ) 
print( "шаг3", numbers[::2] ) # 0 + 2 -> 2 + 2 -> 4 -> 6
print( "шаг4", numbers[:6:10] ) # 0 + 2 -> 2 + 2 -> 4 -> 6

print( numbers[-1])
