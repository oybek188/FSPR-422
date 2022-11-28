"""
Область видимости - Scope
LEGB - Local Enclosed Global Built-in
ЛВГВ - Локальный Вложеный Глобальный Встроенный
"""

# print(print) # built-in

name = "Oybek" # global

def get_name():
    name = "George" # local
    print(name)

# get_name()


# глобальная
name = "Dave"

def spam():
    # локальная
    name = "Guido"

# spam()
# print(name)


# Modifying Global variables
name = "Dave"

def spam():
    global name # импортирует глобальную переменную
    name = "Guido" # Changes the global name above

# spam()
# print(name)



def foo(items):
    items.append(42)

a = [1, 2, 3]
foo(a)
# print(a)    # [1, 2, 3, 42]


# # VS
def bar(items):
    items = [4, 5, 6]

b = [1, 2, 3]
bar(b)
# print('b не поменялось', b) # [1, 2, 3]

a = [1, 2, 3]
b = a
b = [2, 4]
b.append(43)
# print(a, b)


def parent():
    a = 5
    return a

# print("не вложенный", parent()) # 5

# LEGB
# Global
def parent():
    # enclosed
    a = 5
    def answer():
        #local
        a = 10
        def get():
            return a
        return get()
    return answer()

# print("вложенный", parent()) # 5

# Nonlocal variable

def outer():
    # enclosed
    x = "local"

    def inner():
        # local
        nonlocal x
        x = 'non local'
        print('inner:', x)

    inner()
    print('outer', x)

outer()
