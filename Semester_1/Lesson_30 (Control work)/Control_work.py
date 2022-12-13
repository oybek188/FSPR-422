# 1.1. Назовате все типы переменных и их особенности
"""
Изменяемые 
    set - Множество это неупорядоченная последовательность, пишется в фигурных скобках. 
    dict - хранит данные в формате ключ и значение. Получить доступ к значению словаря можно с помощью ключа
    list - упорядоченная последовательность, которая хранит одинаковые элементы
 
Неизменяемые 
    bin - Преобразует целое число в двоичную строку
    frozenset - Множество. Отличие set от frozenset, то что set - изменяемый тип данных, а frozenset - нет
    tuple - Кортеж которая имеет упорядоченость и хранит одинаковые элементы. 
    int - создает целое число округляя его или строкового значение
    float - так же создает число, но используется для дробных
    str - создает строку из таких типов данных как строки и целые числа
    bool - используется для условий False или True
    None - Константа, представляющая отсутствие значения
"""


# 1.2. Какие типы переменных можно хранить в качестве значений множества и ключа словаря
"""
list, set, dict, 
"""


# 1.3. Что такое MRO и наследование в питоне
"""
Наследование - это когда класс наследует атрибуты и методы своего родителя.
Если один класс унаследован от другого, то он от него перенимает себе методы и атрибуты своего родителя. 
Таким образом, когда вы вызываете метод экземпляра класса, Python должен посмотреть, есть ли в нем этот метод. 
Если есть – он и будет вызван, а если его нет, то ему придется проверить классы-родители данного класса, это и есть MRO.
"""


# 1.4. Опишите процесс публикования изменений в гитхаб
"""
git remote add origin "ссылка_на_репозиторий" - Что связать с репозмиторием 
git push --set-upstream origin main - Чтоб указать в какой branch опубликовать
git status - Чтобы узнать ныннешний статус проекта 
git add . - Чтобы добавить все изменения
git commit -m "message" - Чтобы добавить коммит
git push - Чтоб опубликовать все изменения в репозиторий
"""


# 1.5. В чем разница между функцией и методом?
"""
Методы - это функции, являющиеся атрибутами классов. 
Любой метод - функция, но не каждая функция - метод. 
Но никакой принципиальной разницы между ними в нет.
Функция является вызываемым объектом в Python, т.е. может быть вызвана с помощью оператора вызова
Метод – это класс функции и не может быть вызван не передавая экземпляр в качестве аргумента
"""


# 2.1. Перечислите и Приведите пример оператов: сравнения, логических, особые операторы
"""
Операторы сравнения:
 < - «меньше»;
 <= - «меньше или равно;
 == - «равно»;
 != - «не равно»;
 > - «больше»;
 >= - «больше или равно».

Логические операторы:
 and - используется для определения 2 условий
 not - используется для исключения
 or - используется для определения одного из 2 условий

Особые операторы:
 is - True, если операнды идентичны
 is not - True, если операнды не идентичны
"""


# 2.2. Что такое полиморфизм? приведите пример с полиморфизмом (надо создать свой пример)
"""
Полиморфизм - разное поведение одного и того же метода в разных классах. 
Например, мы можем сложить два числа, и можем сложить две строки. 
При этом получим разный результат, так как числа и строки являются разными классами.
"""
print(1 + 1)
# 2
print("1" + "1")
# '11'


# 2.3. Исправьте код. 
"""
В конце вы должны создать код по проверке данных ползователя 
и возвращает сообщение об успешном или проваленном логине.
def validate(username, password):
    username "Random" password 2321ewfsef
    return "Вы успешно вошли в систему!"
    return Пароль или имя пользователя не правильны
"""
def validate():
    username = str(input("Введите имя пользователя: "))
    password = str(input("Введите пароль: "))
    if username == "Random" and password == "2321ewfsef":
        return print("Вы успешно вошли в систему!")
    else:
        return print("Пароль или имя пользователя не правильны!")
validate()


# 2.4. Приведете список областей видимости в питоне и пример с каждым из них.
"""
Локальная область видимости
Глобальная область видимости
"""
name = "Oybek" # Глобальная область

def get_name():
    """Локальная область"""
    name = "Sherzod"
    print(name)

get_name()


# 2.5. Описать что такое рекурсия и пример с нахождением чисел фиббоначи.
"""
Рекурсия — это способ организации циклического процесса путем вызова рекурсивной функции. 
Рекурсивная функция — это функция, которая содержит код вызова самой себя с целью организации циклического процесса. 
С помощью рекурсивных функций можно с минимальным объемом кода решать некоторые задачи, 
обойдя использование лишних структур данных. 
Рекурсию можно рассматривать как альтернативу циклам

"""
def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Введите число последовательности:"))
print("Последовательность Фибоначчи:")
for i in range(n):
    print(fibonacci(i))


# 3.1. Исправьте код ниже. 
"""
После исправления код должен возваращть все аргументы, которые были приняты в виде списка other_info и выводить их на экран:
def get_data(**kwargs, code, *args, salary):
    other_info = []
    for arg in args
print(arg)
    for key, val in kwargs:
    other_infoappend((key, val))

    return other_info
"""
def get_data(code,  salary, *args, **kwargs, ):
    other_info = []
    for arg in args
print(arg)
    for key, val in kwargs:
    other_infoappend((key, val))

    return other_info
    