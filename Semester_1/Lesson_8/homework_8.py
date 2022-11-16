print("Задание №1")
print("Написать код, который реализует то, что делает функция isinstance и сделать проверку на то, является ли перменная строкой или числом")
print(sep="\n\n")

try:
    x = float(input('Введите значение: '))
    print('Значение является числом')
except:
    print('Значение является строкой')
    
# print( "Пременная является строкой" if x == str else "Пременная не является строкой")


# print(sep="\n\n")
# print("Задание №2")
# print("""
# 2. Принять через Input 3 значения: xp (int), damage (int), mp (int). Сравнить эти числа и если 
# xp<=100 damage<=10 mp<=50 -> "Уровень 1"
# xp<=300 damage<=20 mp<=100 -> "Уровень 10"
# xp<=500 damage<=100 mp<=200 -> "Уровень 15" 
# Если больше этого -> "Вы герой"
# """)
# print(sep="\n\n")

# xp = int(input("Введите значение XP: "))
# damage = int(input("Введите значение Damage: "))
# mp = int(input("Введите значение MP: "))
# if xp <= 100 and damage <= 10 and mp <= 50:
#     print("Уровень 1")
# elif xp <= 300 and damage <= 20 and mp <= 100:
#     print("Уровень 10")
# elif xp <= 500 and damage <= 100 and mp <= 200:
#     print("Уровень 15")
# elif xp > 500 and damage > 100 and mp > 200:
#     print("Вы герой")
