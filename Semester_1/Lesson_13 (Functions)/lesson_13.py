def shades_of_grey(n):
    shades = []
    hex = "123456789abcdef"
    counter = 0
    for i in range(n):
        if counter == 15:
            counter = 0
        gray = f"#0{hex[counter]}0{hex[counter]}0{hex[counter]}"
        if i >= 15:
            gray = f"#1{hex[counter]}1{hex[counter]}1{hex[counter]}"
        shades.append(gray)
        counter += 1
        
    return shades
print(shades_of_grey(16))


# Написать функцию, которая принимает два аргумента: n и num - и на основе них, создает список. 
# n для опрделения длины списка. num умножить на все значения в списке. Значениями списка могут быть числа, 
# которые вы получаете из цикла

def create_list(n, num):
    numbers = []
    for i in range(n):
        numbers.append(i * num)
    return numbers
print(create_list(20, 2))
print(create_list(10, 5))


def func(a, default="hi"):
    print(a, default)

func(12)
func(12, "not hi")

def func(a, b, default="hi"):
    print("a =", a, "b =", b, default)

# func(12)
# func(12, "not hi")
# func(12, 5, "not hi")

# арги
def func(a, b, default="hi", *args):
    print(a, b, "default=", default, "args=", args)

func(12, 4, "yeah", 3, 4, [2, 3, 4])

def any_arg(*args):
    """Функция, которая принимает любое количество аргументов и выводит их на экран."""
    print("args=", args)
    for arg in args:
        print(arg)

any_arg(2, 3, 4, "goo", "nooo", {1 : 1}, [], {3, 4, 5})
any_arg()