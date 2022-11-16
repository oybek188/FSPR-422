# Правило передачи аргументов
from psutil import users
from traitlets import default


def order_of_args(name, default="go", *args, sep="separator", username, end="\n", **kwargs):
    print(name, default, args, username, end, sep, kwargs)

order_of_args("Oybek", 123, 4, 5, 6, username="apo", end="not enter", sep="not sep", email="e@com", loot=[2, 3])


# Создать функцию, которая принимает любые аргументы
def func(*args, **kwargs):
    print(args, kwargs)

func("name", 2, 3, 4, 5, user={"name": "Ya"}, goal=("champion"))


